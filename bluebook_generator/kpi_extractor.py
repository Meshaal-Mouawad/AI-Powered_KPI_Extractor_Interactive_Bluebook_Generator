import os
import re
from typing import List, Dict, Tuple
# Scanner performance knobs
IGNORE_DIRS = {".git", ".hg", ".svn", "node_modules", "dist", "build", "__pycache__", ".venv", "venv", ".mypy_cache", ".pytest_cache"}
ALLOWED_EXTS = {".py", ".sql", ".ps1", ".dax", ".cs", ".vb", ".abap", ".st", 
                 ".hdbview", ".hdbprocedure", ".hdbfunction", ".hdbtablefunction", ".sqlscript",
                 ".tsql", ".pks", ".pkb", ".pls", ".txt", ".csv"}
MAX_FILE_MB = float(os.environ.get("KPI_MAX_FILE_MB", "2"))  # default 2 MB

# Optional formula extraction from comments like "Formula: ..."
try:
    from .parser import extract_formula_from_comments as _extract_formula_from_comments
except Exception:
    _extract_formula_from_comments = None

__all__ = ["find_kpis_in_directory"]


# ---------- Supported extensions (language hint) ----------

_SUPPORTED_EXTS = {
    # Python
    ".py": "python",
    # .NET family
    ".cs": "csharp",
    ".vb": "vbnet",
    # SQL families (ANSI SQL, T-SQL, Oracle/PLSQL, HANA SQLScript)
    ".sql": "sql",
    ".tsql": "tsql",  # T‑SQL specific files
    ".pks": "plsql",
    ".pkb": "plsql",
    ".pls": "plsql",
    # SAP HANA SQLScript artifacts
    ".hdbprocedure": "hana",
    ".hdbfunction": "hana",
    ".hdbview": "hana",
    ".hdbtablefunction": "hana",
    ".sqlscript": "hana",
    # SAP ABAP
    ".abap": "abap",
    # Power BI DAX (text exports)
    ".dax": "dax",
    ".dax.txt": "dax",
    # IEC 61131‑3 Structured Text / PLC textual files
    ".st": "iec_st",
    ".scl": "iec_st",   # Siemens SCL
    ".awl": "iec_st",   # STL/AWL textual
    # Generic text/CSV exports (Excel/BI/SAP dumps)
    ".txt": "text",
    ".csv": "csv",
}


# ---------- Utilities ----------

def _read_text_file_safe(path: str, max_bytes: int = 2_000_000) -> str:
    """Read small text files safely; skip very large or unreadable files.
    """
    try:
        if os.path.getsize(path) > max_bytes:
            return ""
    except Exception:
        return ""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""


def _window(lines: List[str], center: int, before: int = 10, after: int = 20) -> str:
    """Return a small window of text lines around a center line number."""
    start = max(0, center - before)
    end = min(len(lines), center + after + 1)
    return "\n".join(lines[start:end])


def _expand_forward_statement(lines: List[str], start_index: int, back: int = 5, max_forward: int = 200) -> str:
    """Return a forward-expanded SQL-ish statement context starting a few lines before start_index.

    - Includes up to `back` lines before the start_index for context.
    - Scans forward up to `max_forward` lines or until a likely statement terminator is seen:
      semicolon at low parenthesis depth, a lone GO, or end of file.
    - Works for SQL/T-SQL/PLSQL/HANA snippets where KPI comment precedes a CREATE/SELECT.
    """
    import re as _re

    n = len(lines)
    if n == 0:
        return ""

    start = max(0, min(start_index, n - 1))
    ctx_start = max(0, start - back)

    end = start
    depth = 0
    for j in range(start, min(n, start + max_forward)):
        line = lines[j].rstrip("\n")
        end = j
        # Track parentheses depth to avoid stopping too early inside CAST(...), CASE(...), etc.
        depth += line.count("(") - line.count(")")
        if _re.search(r";\s*$", line) and depth <= 0:
            break
        if _re.match(r"^\s*GO\s*$", line, _re.I):
            break
        if _re.match(r"^\s*/\s*$", line):  # Oracle '/' statement separator on its own line
            break

    return "\n".join(l.rstrip("\n") for l in lines[ctx_start:end + 1])


def _normalize_name(raw: str) -> str:
    name = (raw or "").strip()
    name = re.sub(r'^[\[\("\']+|[\]\)"\']+$', "", name).strip()
    name = re.sub(r'[_\s]+', " ", name)
    return name


def _extract_by_comment_tag(lines: List[str], pattern: re.Pattern, language: str) -> List[Dict]:
    """Capture `KPI: Name` markers using a language-specific comment pattern."""
    out = []
    for i, line in enumerate(lines):
        m = pattern.search(line)
        if not m:
            continue
        name = _normalize_name(m.group("name"))
        out.append({
            "name": name,
            "language": language,
            "file_line": i + 1,
            "code_context": _window(lines, i),
            "_rank": 1,  # base rank for comment hits
            "_kind": "comment"
        })
    return out

def _extract_python(text: str) -> List[Dict]:
    lines = text.splitlines()
    out: List[Dict] = []

    # # KPI: Name
    out += _extract_by_comment_tag(lines, re.compile(r"#\s*KPI\s*:\s*(?P<name>.+)$", re.I), "python")

    # Functions with KPI-ish names
    for i, line in enumerate(lines):
        m = re.search(r"\bdef\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", line)
        if not m:
            continue
        fn = m.group(1)
        if any(k in fn.lower() for k in ("kpi", "yield", "percentage", "ratio", "throughput", "oee", "variance", "recovery", "cost", "emission")):
            out.append({
                "name": _normalize_name(fn.replace("_", " ")),
                "language": "python",
                "file_line": i + 1,
                "code_context": _window(lines, i),
            })
    return out


def _extract_csharp_vb(text: str, language: str) -> List[Dict]:
    lines = text.splitlines()
    out: List[Dict] = []

    # C# attribute form: [KPI("Name")]
    for i, line in enumerate(lines):
        m = re.search(r"\[\s*KPI(?:Attribute)?\s*\(\s*\"(?P<name>[^\"]+)\"\s*\)\s*\]", line, re.I)
        if m:
            out.append({
                "name": _normalize_name(m.group("name")),
                "language": language,
                "file_line": i + 1,
                "code_context": _window(lines, i, 5, 60),  # widened after-context for Return
            })

    # C#: // KPI: Name
    out += _extract_by_comment_tag(lines, re.compile(r"//\s*KPI\s*:\s*(?P<name>.+)$", re.I), language)
    # VB.NET: ' KPI: Name
    out += _extract_by_comment_tag(lines, re.compile(r"'\s*KPI\s*:\s*(?P<name>.+)$", re.I), language)

    # Methods like CalculateXxxKpi(...)
    for i, line in enumerate(lines):
        m = re.search(r"\b(Calculate|Compute)[A-Za-z0-9_]*Kpi\s*\(", line, re.I)
        if m:
            name = _normalize_name(m.group(0).split("(")[0])
            out.append({
                "name": name,
                "language": language,
                "file_line": i + 1,
                "code_context": _window(lines, i, 5, 60),
            })
    return out


def _extract_sql_like(text: str, dialect: str) -> List[Dict]:
    lines = text.splitlines()
    out: List[Dict] = []

    # Normalize potential BOM and EOL noise
    stripped_lines = [ln.lstrip("\ufeff").rstrip("\r\n") for ln in lines]

    # 1) Prefer explicit KPI lines:
    comments = []
    # Match "-- KPI: ..." or "// KPI: ..." (tolerant to leading spaces/BOM)
    for i, line in enumerate(stripped_lines):
        m = re.search(r"^\s*(?:--|//)\s*KPI\s*:\s*(?P<name>.+)$", line, re.I)
        if m:
            comments.append((i, _normalize_name(m.group("name"))))
    # Match "/* KPI: ... */" (inline)
    for i, line in enumerate(stripped_lines):
        m = re.search(r"/\*\s*KPI\s*:\s*(?P<name>[^*]+)\*/", line, re.I)
        if m:
            comments.append((i, _normalize_name(m.group("name"))))
    # NEW: also match bare "KPI: ..." even if not in a comment (safety net)
    if not comments:
        for i, line in enumerate(stripped_lines):
            m = re.search(r"\bKPI\s*:\s*(?P<name>.+)$", line, re.I)
            if m:
                comments.append((i, _normalize_name(m.group("name"))))
                break

    for i, name in comments:
        out.append({
            "name": name,
            "language": dialect,
            "file_line": i + 1,
            "code_context": _expand_forward_statement(lines, i),
            "_rank": 3,
            "_kind": "sql_comment"
        })

    has_comment = len(comments) > 0

    # 2) Fallbacks if no comment matched:
    if not has_comment:
        # 2a) CREATE FUNCTION <any_name> (be tolerant; not only kpi_*)
        for i, line in enumerate(stripped_lines):
            m = re.search(
                r"\bcreate\s+(?:or\s+replace\s+)?function\s+(?P<fn>[A-Za-z0-9_\.$]+)",
                line, re.I
            )
            if m:
                fn_name = _normalize_name(m.group("fn"))
                out.append({
                    "name": fn_name,
                    "language": dialect,
                    "file_line": i + 1,
                    "code_context": _expand_forward_statement(lines, i),
                    "_rank": 2,
                    "_kind": "create_function"
                })
                # Keep scanning; multiple functions are possible

        # 2b) CREATE VIEW view_kpi_* AS ...
        for i, line in enumerate(stripped_lines):
            m = re.search(r"\bcreate\s+view\s+([A-Za-z0-9_\.]*kpi[A-Za-z0-9_\.]*)\b", line, re.I)
            if m:
                out.append({
                    "name": _normalize_name(m.group(1)),
                    "language": dialect,
                    "file_line": i + 1,
                    "code_context": _window(lines, i, 5, 120),
                    "_rank": 2,
                    "_kind": "create_view"
                })

        # 2c) SELECT ... expr AS alias (alias contains kpi_* or measure_*)
        for i, line in enumerate(stripped_lines):
            m = re.search(r"\bas\s+(kpi[_A-Za-z0-9]+|measure[_A-Za-z0-9]+)\b", line, re.I)
            if m:
                out.append({
                    "name": _normalize_name(m.group(1)),
                    "language": dialect,
                    "file_line": i + 1,
                    "code_context": _window(lines, i, 3, 80),
                    "_rank": 2,
                    "_kind": "select_alias"
                })

        # 2d) LAST-RESORT (PL/SQL only): if we see a math RETURN, emit one KPI using the file name
        if dialect.lower() in {"plsql"} and not out:
            # Look for a mathy RETURN in the whole text
            if re.search(r"(?is)\breturn\b.+[*/+-].+", text):
                base_name = "PLSQL KPI"
                # Derive a human-ish name from the file if available
                try:
                    import os as _os
                    base_name = _normalize_name(_os.path.splitext(_os.path.basename(__file__ if False else ""))[0]) or "PLSQL KPI"
                except Exception:
                    pass
                # Use a wide context: the whole file, so formula extractor can grab the RETURN expression
                out.append({
                    "name": base_name,
                    "language": dialect,
                    "file_line": 1,
                    "code_context": text,
                    "_rank": 1,
                    "_kind": "plsql_return_fallback"
                })

    return out


def _extract_hana(text: str) -> List[Dict]:
    """
    SAP HANA SQLScript artifacts often embed SQLScript with comments like -- or /* ... */.
    Handle both SQL-like content and JSON-style .hdbview definitions.
    """
    # 1) Try SQL-like first
    out = _extract_sql_like(text, "hana")
    if out:
        return out

    # 2) JSON-style .hdbview fallback
    try:
        import json
        obj = json.loads(text)
        vd = (obj.get("viewDefinition") or {})
        cols = vd.get("columns") or []
        best = None
        for c in cols:
            name = (c.get("name") or "").strip()
            expr = (c.get("expression") or "").strip()
            if not name or not expr:
                continue
            score = 1
            if "kpi" in name.lower():
                score += 2
            if any(ch in expr for ch in "*/+-"):
                score += 1
            best = max([best, (score, name, expr)] if best else [(score, name, expr)], key=lambda t: t[0])
        if best:
            _, name, expr = best
            code = f"SELECT {expr} AS {name}"
            return [{
                "name": _normalize_name(name),
                "language": "hana",
                "file_line": 1,
                "code_context": code,
            }]
    except Exception:
        pass

    return []


def _extract_tsql(text: str) -> List[Dict]:
    """T‑SQL specific files (.tsql) → reuse SQL-like extraction with label 'tsql'."""
    return _extract_sql_like(text, "tsql")




def _extract_plsql(text: str) -> List[Dict]:
    """PL/SQL files (.pks/.pkb/.pls) → reuse SQL-like extraction with label 'plsql'."""
    out = _extract_sql_like(text, "plsql")
    if out:
        return out
    # Fallback for .pks package spec: capture FUNCTION signatures
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.search(r"\bFUNCTION\s+([A-Za-z0-9_\.$]+)", line, re.I)
        if m:
            fn = _normalize_name(m.group(1))
            return [{
                "name": fn,
                "language": "plsql",
                "file_line": i + 1,
                "code_context": _window(lines, i),
            }]
    return out


def _extract_dax(text: str) -> List[Dict]:
    """Power BI DAX code."""
    lines = text.splitlines()
    out: List[Dict] = []
    seen_names = set()

    # DEFINE MEASURE 'Table'[Measure] = ...
    for i, line in enumerate(lines):
        m = re.search(r"\bDEFINE\s+MEASURE\s+[^\[]*\[(?P<name>[^\]]+)\]\s*=", line, re.I)
        if m:
            name = _normalize_name(m.group("name"))
            seen_names.add(name.lower())
            out.append({
                "name": name,
                "language": "dax",
                "file_line": i + 1,
                "code_context": _window(lines, i),
            })

    # Simple measure lines: Name = Expression
    for i, line in enumerate(lines):
        if re.match(r"\s*(VAR|RETURN|EVALUATE)\b", line, re.I):
            continue
        m = re.search(r"(?P<name>[A-Za-z0-9 _\[\]\.]+?)\s*=\s*.+", line)
        if m:
            name = _normalize_name(m.group("name"))
            if name.lower() not in seen_names and len(name.strip()) > 2:
                seen_names.add(name.lower())
                out.append({
                    "name": name,
                    "language": "dax",
                    "file_line": i + 1,
                    "code_context": _window(lines, i),
                })

    # -- KPI: Name (only add if not already captured as a measure)
    for i, line in enumerate(lines):
        m = re.search(r"--\s*KPI\s*:\s*(?P<name>.+)$", line, re.I)
        if m:
            name = _normalize_name(m.group("name"))
            if name.lower() not in seen_names:
                out.append({
                    "name": name,
                    "language": "dax",
                    "file_line": i + 1,
                    "code_context": _window(lines, i),
                })
    return out


def _extract_abap(text: str) -> List[Dict]:
    lines = text.splitlines()
    out: List[Dict] = []

    # "* KPI: Name"
    out += _extract_by_comment_tag(lines, re.compile(r"\*\s*KPI\s*:\s*(?P<name>.+)$", re.I), "abap")

    # REPORT ... KPI ...
    for i, line in enumerate(lines):
        if re.search(r"\bREPORT\b.*\bKPI\b", line, re.I):
            out.append({
                "name": _normalize_name(line),
                "language": "abap",
                "file_line": i + 1,
                "code_context": _window(lines, i),
            })
    return out


def _extract_iec_st(text: str) -> List[Dict]:
    """
    IEC 61131‑3 Structured Text and PLC textual code.
    Comment styles: // line comment, (* block comment *), and sometimes {**}.
    We rely primarily on explicit 'KPI:' tags in comments.
    """
    lines = text.splitlines()
    out: List[Dict] = []

    # // KPI: Name
    out += _extract_by_comment_tag(lines, re.compile(r"//\s*KPI\s*:\s*(?P<name>.+)$", re.I), "iec_st")

    # (* KPI: Name *)
    for i, line in enumerate(lines):
        m = re.search(r"\(\*\s*KPI\s*:\s*(?P<name>[^*]+)\*\)", line, re.I)
        if m:
            out.append({
                "name": _normalize_name(m.group("name")),
                "language": "iec_st",
                "file_line": i + 1,
                "code_context": _window(lines, i),
            })

    # {** KPI: Name **}
    for i, line in enumerate(lines):
        m = re.search(r"\{\*+\s*KPI\s*:\s*(?P<name>[^*]+)\*+\}", line, re.I)
        if m:
            out.append({
                "name": _normalize_name(m.group("name")),
                "language": "iec_st",
                "file_line": i + 1,
                "code_context": _window(lines, i),
            })

    return out


def _extract_generic(text: str) -> List[Dict]:
    """Fallback extractor for miscellaneous text files."""
    lines = text.splitlines()
    out: List[Dict] = []
    # Support common comment styles in mixed text
    out += _extract_by_comment_tag(lines, re.compile(r"#\s*KPI\s*:\s*(?P<name>.+)$", re.I), "generic")
    out += _extract_by_comment_tag(lines, re.compile(r"//\s*KPI\s*:\s*(?P<name>.+)$", re.I), "generic")
    out += _extract_by_comment_tag(lines, re.compile(r"--\s*KPI\s*:\s*(?P<name>.+)$", re.I), "generic")
    for i, line in enumerate(lines):
        m = re.search(r"/\*\s*KPI\s*:\s*(?P<name>[^*]+)\*/", line, re.I)
        if m:
            out.append({
                "name": _normalize_name(m.group("name")),
                "language": "generic",
                "file_line": i + 1,
                "code_context": _window(lines, i),
            })
    return out


# ---------- Dispatcher ----------

def _detect_language_by_extension(path_lower: str) -> str:
    """Map file extension to a language."""
    for ext, lang in _SUPPORTED_EXTS.items():
        if path_lower.endswith(ext):
            return lang
    return "generic"


def _extract_from_text(text: str, language_hint: str) -> List[Dict]:
    lang = language_hint
    if lang == "python":
        return _extract_python(text)
    if lang in ("csharp", "vbnet"):
        return _extract_csharp_vb(text, lang)
    if lang in ("sql",):
        return _extract_sql_like(text, "sql")
    if lang == "tsql":
        return _extract_tsql(text)
    if lang == "plsql":
        return _extract_plsql(text)
    if lang == "hana":
        return _extract_hana(text)
    if lang == "dax":
        return _extract_dax(text)
    if lang == "abap":
        return _extract_abap(text)
    if lang == "iec_st":
        return _extract_iec_st(text)
    return _extract_generic(text)


# ---------- Public API ----------

def find_kpis_in_directory(root_path: str) -> List[Dict]:
    """
    Walk a directory tree and extract KPI candidates across multiple languages.

    Returns a list of dicts with at most one KPI per file (best guess), using
    simple, deterministic preference:
      - Prefer items that came from comment tags or explicit constructs (higher _rank).
      - If ranks equal, prefer names that look human (contain spaces or parentheses).
    """
    results: List[Dict] = []
    if not root_path:
        return results

    try:
        base = os.path.expanduser(root_path)
        if not os.path.isabs(base):
            base = os.path.abspath(base)
        if not os.path.isdir(base):
            return results
    except Exception:
        return results
    for dirpath, dirnames, filenames in os.walk(base):  # FIX: use `base` (not base_path)
        # prune directories in-place
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith('.')]

        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if ALLOWED_EXTS and ext not in ALLOWED_EXTS:
                continue

            path = os.path.join(dirpath, fn)

            # size filter
            try:
                if os.path.getsize(path) > MAX_FILE_MB * 1024 * 1024:
                    continue
            except OSError:
                continue

            # Detect language (FIX: define p_lower before using it)
            p_lower = path.lower()
            lang = _detect_language_by_extension(p_lower)

            # Read file safely
            text = _read_text_file_safe(path)
            if not text:
                continue

            # Extract KPIs for this file
            try:
                file_kpis = _extract_from_text(text, lang) or []
            except Exception:
                file_kpis = []

            # Attach file path and accumulate
            for k in file_kpis:
                k["file_path"] = path
                # Try to extract an explicit formula from comments if helper available
                if _extract_formula_from_comments:
                    try:
                        formula = _extract_formula_from_comments(text.splitlines())
                        if formula:
                            k["formula"] = formula
                    except Exception:
                        pass

            if not file_kpis:
                continue

            # Pick a single best KPI per file (FIX: define `human`)
            def rank(item: Dict) -> Tuple[int, int]:
                r = int(item.get("_rank", 0))
                n = item.get("name") or ""
                human = 1 if re.search(r"[ ()\[\]]", n) else 0  # prefer names with spaces/paren/brackets
                return (r, human)

            best = max(file_kpis, key=rank)

            # Strip internal helper fields
            best.pop("_rank", None)
            best.pop("_kind", None)

            results.append(best)

    return results