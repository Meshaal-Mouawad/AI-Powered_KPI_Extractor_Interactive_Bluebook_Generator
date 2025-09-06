import os
import json
import time
from typing import Dict, Any, List, Tuple
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
from .kpi_extractor import find_kpis_in_directory


import re
import ast
import numpy as np  # used only for cosine similarity

# Explicitly export public API to avoid "cannot import name" issues

# ---- Lightweight Knowledge Base (KB) + Overrides integration ----

def _kb_file_path() -> str:
    # Put your curated petrochemical KPI KB here (optional). Example schema below.
    # Path is relative to project root; adjust as needed.
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "bluebook_generator", "kb", "petro_kpi_kb.json")

def _overrides_file_path() -> str:
    # Stores user edits by KPI name. Created on first edit.
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs", "overrides.json")

def _safe_load_json(path: str) -> Any:
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        pass
    return None

def _get_text_embedding(client: OpenAI, text: str) -> List[float]:
    # Small, inexpensive embedding for retrieval
    emb = client.embeddings.create(model="text-embedding-3-small", input=text)
    return emb.data[0].embedding

def _cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)

def _retrieve_kb_examples(client: OpenAI, kpi_name: str, top_k: int = 3) -> List[Dict[str, Any]]:
    """
    Returns up to top_k KB items most similar to the KPI name.
    KB item schema example:
      {
        "name": "Polymer Melt Flow Index (MFI) Variance",
        "description": "Measures the variability ...",
        "objective": "...",
        "input_measure": "...",
        "unit_of_measure": "dimensionless",
        "reporting_source": "Laboratory test results ..."
      }
    """
    kb_path = _kb_file_path()
    kb = _safe_load_json(kb_path)
    if not kb or not isinstance(kb, list):
        return []

    try:
        query_emb = np.array(_get_text_embedding(client, kpi_name), dtype=np.float32)
    except Exception:
        return []

    ranked: List[Tuple[float, Dict[str, Any]]] = []
    for item in kb:
        text = f"{item.get('name','')} {item.get('description','')} {item.get('objective','')}"
        try:
            emb = np.array(_get_text_embedding(client, text), dtype=np.float32)
            ranked.append((_cosine_sim(query_emb, emb), item))
        except Exception:
            continue

    ranked.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in ranked[:top_k]]

def _load_user_overrides_for(kpi_name: str) -> Dict[str, Any]:
    """
    overrides.json structure:
    {
      "KPI Name": {
        "description": "...",
        "objective": "...",
        "input_measure": "...",
        "unit_of_measure": "...",
        "reporting_source": "...",
        "comments": "..."
      },
      ...
    }
    """
    path = _overrides_file_path()
    data = _safe_load_json(path)
    if isinstance(data, dict):
        return data.get(kpi_name, {}) or {}
    return {}

_GENERIC_PHRASES = {
    "desc": [
        "is a key performance indicator used to assess process efficiency and operational performance",
    ],
    "obj": [
        "provide a clear measure that supports monitoring",
        "decision making",
        "continuous improvement",
    ],
    "used": [
        "can serve as an input to higher-level operational and performance dashboards",
    ],
    "input": [
        "derived from the variables used in the code calculation for this kpi",
    ],
    "comments_empty": [
        "no additional comments or special considerations were provided for this kpi",
    ],
}

def _is_generic_text(text: str | None, kind: str) -> bool:
    if not text:
        return True
    t = text.strip().lower()
    patterns = _GENERIC_PHRASES.get(kind, [])
    return any(p in t for p in patterns)

def _append_sentence_if_missing(text: str, sentence: str) -> str:
    text = (text or "").strip()
    if not text:
        return sentence
    if sentence and sentence.lower() not in text.lower():
        return f"{text} {sentence}"
    return text

# NEW: strict single-category classifier based on KPI name only
def _classify_kpi(kpi_name: str) -> str | None:
    n = (kpi_name or "").lower()
    # Order matters: pick the most specific first
    if "mfi" in n or "melt flow index" in n:
        return "mfi_variance"
    if "propyl" in n and "ethyl" in n or "p/e" in n:
        return "pe_ratio"
    if "on-spec" in n or "on spec" in n or "on_spec" in n:
        return "on_spec_percentage"
    if "flare" in n and "recover" in n:
        return "flare_recovery_rate"
    if "throughput" in n:
        return "throughput"
    if "yield" in n and "percentage" in n:
        return "yield_percentage"
    if "oee" in n or "overall equipment effectiveness" in n:
        return "oee"
    if "specific catalyst cost" in n:
        return "specific_catalyst_cost"
    return None

def _enrich_with_domain_hints(kpi_name: str, code_context: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge generic fields with domain-aware sentences. Exactly ONE category applies,
    chosen from the KPI name to avoid cross-contamination between KPIs.
    """
    category = _classify_kpi(kpi_name)
    ctx = (code_context or "").lower()

    def set_if_generic(field: str, value: str):
        current = data.get(field, "") or ""
        data[field] = value if _is_generic_text(
            current,
            "desc" if field == "description" else
            "obj" if field == "objective" else
            "used" if field == "used_in_kpis" else
            "input" if field == "input_measure" else
            "comments_empty" if field == "comments" else "desc"
        ) else _append_sentence_if_missing(current, value)

    uom = (data.get("unit_of_measure") or "").strip().lower()
    src = (data.get("reporting_source") or "").strip().lower()

    if category == "mfi_variance":
        set_if_generic("description",
            "The Polymer Melt Flow Index (MFI) Variance measures the variability in the melt flow index of polymer samples and indicates how easily the polymer flows when melted.")
        set_if_generic("objective",
            "Monitoring MFI variance helps ensure consistent product quality and process stability; low variance suggests a stable process and adherence to quality standards.")
        set_if_generic("input_measure",
            "Melt Flow Index test results from polymer samples collected during production or laboratory testing.")
        set_if_generic("used_in_kpis",
            "Used in quality control and assurance to evaluate polymer production performance and detect potential manufacturing issues.")
        if uom in {"", "variance (units^2)", "unit not specified", "n/a"}:
            data["unit_of_measure"] = "dimensionless"
        if not src or "histor" in src or "logs" in src:
            data["reporting_source"] = "Laboratory test results of polymer samples taken during production."
        set_if_generic("comments",
            "Tracking MFI variance is essential for maintaining product quality and ensuring products meet required specifications for intended applications.")

    elif category == "pe_ratio":
        set_if_generic("description",
            "The ratio of propylene to ethylene production volumes, used to assess the balance of the product slate.")
        set_if_generic("objective",
            "Align production strategy with market demand and margins by monitoring relative propylene versus ethylene output.")
        set_if_generic("input_measure",
            "Total propylene produced and total ethylene produced in the measurement period.")
        if uom in {"", "unit not specified", "n/a"}:
            data["unit_of_measure"] = "ratio (dimensionless)"
        if not src:
            data["reporting_source"] = "Process historian (e.g., AVEVA PI System) and control system archives."

    elif category == "on_spec_percentage":
        set_if_generic("description",
            "This KPI expresses the proportion of production that meets all quality standards relative to total batches.")
        set_if_generic("objective",
            "Improve first-pass quality and reduce rework or off-spec material by monitoring on-spec performance over time.")
        set_if_generic("input_measure",
            "Counts of on-spec batches and total batches in the measurement period.")
        if uom in {"", "unit not specified", "n/a"}:
            data["unit_of_measure"] = "%"
        if not src:
            data["reporting_source"] = "Process historian and quality management/execution system records."

    elif category == "flare_recovery_rate":
        set_if_generic("description",
            "Share of total gas that is recovered instead of flared, indicating the effectiveness of recovery systems.")
        set_if_generic("objective",
            "Reduce flaring and emissions by improving recovery system reliability and operation.")
        set_if_generic("input_measure",
            "Gas flared volume and gas recovered volume over the measurement period.")
        if uom in {"", "unit not specified", "n/a", "variance (units^2)"}:
            data["unit_of_measure"] = "%"
        if not src:
            data["reporting_source"] = "Process historian (flare meters and recovery system flow meters)."

    elif category == "throughput":
        set_if_generic("description",
            "Average processing rate of material over the measurement period, typically normalized to daily capacity.")
        set_if_generic("objective",
            "Maximize utilization while respecting equipment and constraint limits.")
        set_if_generic("input_measure",
            "Total feedstock processed and the number of operating hours in the measurement period.")
        if ("* 24" in ctx or "*24" in ctx) and ("/ hours" in ctx or "/hours" in ctx or "hours_online" in ctx):
            data["unit_of_measure"] = "tons/day"
        elif uom in {"", "unit not specified", "n/a"}:
            data["unit_of_measure"] = "tons/hour"
        if not src:
            data["reporting_source"] = "Process historian (e.g., AVEVA PI System) and control system archives."

    elif category == "yield_percentage":
        set_if_generic("description",
            "Proportion of desired product produced relative to total input, indicating conversion efficiency.")
        set_if_generic("objective",
            "Improve conversion efficiency and identify losses or off-spec production by trending yield over time.")
        set_if_generic("input_measure",
            "Desired product output and corresponding input over the measurement period.")
        if uom in {"", "unit not specified", "n/a"}:
            data["unit_of_measure"] = "%"
        if not src:
            data["reporting_source"] = "Process historian and production execution logs."

    elif category == "oee":
        set_if_generic("description",
            "Overall Equipment Effectiveness combines Availability, Performance, and Quality into a single effectiveness score.")
        set_if_generic("objective",
            "Increase effective productive time by reducing downtime, speed losses, and quality losses.")
        set_if_generic("input_measure",
            "Availability, performance, and quality factors calculated for the asset or line.")
        if uom in {"", "unit not specified", "n/a"}:
            data["unit_of_measure"] = "%"
        if not src:
            data["reporting_source"] = "MES/Production systems and equipment runtime counters."

    elif category == "specific_catalyst_cost":
        set_if_generic("description",
            "Cost of catalyst consumed per ton of product, used to monitor and optimize catalyst usage.")
        set_if_generic("objective",
            "Control catalyst spend while maintaining performance and product quality.")
        set_if_generic("input_measure",
            "Catalyst cost used and product tons over the measurement period.")
        if uom in {"", "unit not specified", "n/a"}:
            data["unit_of_measure"] = "currency per ton"
        if not src:
            data["reporting_source"] = "ERP/finance records and production totals from historians or MES."

    # If after enrichment comments remain empty, ensure non-empty default
    if _is_generic_text(data.get("comments"), "comments_empty"):
        data["comments"] = "No additional comments or special considerations were provided for this KPI."
    return data

# ------------------ Existing helpers (restored) ------------------
def _infer_unit_of_measure(kpi_name: str, code_context: str, current_value: str | None) -> str:
    """
    Best-effort unit inference from KPI name and code context.
    Only overrides if current_value is missing or looks generic.
    """
    def is_generic(v: str | None) -> bool:
        if not v:
            return True
        v_low = v.strip().lower()
        return (
            v_low == "n/a"
            or "see calculation" in v_low
            or "not specified" in v_low
            or "context" in v_low
            or len(v_low) < 3
        )

    if not is_generic(current_value):
        return current_value

    name = (kpi_name or "").lower()
    ctx = (code_context or "").lower()

    if "tons/day" in name or "ton/day" in name:
        return "tons/day"
    if "oee" in name or "overall equipment effectiveness" in name:
        return "%"
    if "yield" in name or "percentage" in name:
        return "%"
    if "ratio" in name:
        return "ratio (dimensionless)"
    if "mtbf" in name or "mean time between failures" in name:
        return "hours per failure"

    if "tons/day" in ctx or "ton/day" in ctx:
        return "tons/day"
    if "np.var(" in ctx or "variance" in ctx:
        return "variance (units^2)"

    if "throughput" in name or "throughput" in ctx:
        has_tons = "ton" in ctx or "tons" in ctx
        divides_hours = "/ hours" in ctx or "/hours" in ctx or " / 24" in ctx
        times_24 = "* 24" in ctx or "*24" in ctx
        if has_tons and divides_hours and times_24:
            return "tons/day"
        if has_tons and divides_hours:
            return "tons/hour"

    if "* 100" in ctx or "*100" in ctx:
        return "%"

    return current_value or "unit not specified"

def _infer_reporting_source(code_context: str, current_value: str | None) -> str:
    """
    Provide a more specific reporting source when the current value looks generic or empty.
    """
    def is_generic(v: str | None) -> bool:
        if not v:
            return True
        v_low = v.strip().lower()
        return (
            v_low.startswith("typically sourced")
            or v_low in {"n/a", "not specified"}
            or len(v_low) < 3
        )

    if not is_generic(current_value):
        return current_value

    ctx = (code_context or "").lower()

    if any(k in ctx for k in ["histori", "pi system", "osisoft", "aveva", "processbook"]):
        return "Process historian (e.g., AVEVA PI System) and control system archives."
    if any(k in ctx for k in ["opc", "scada", "dcs", "plc"]):
        return "SCADA/DCS via OPC/PLC tags."
    if any(k in ctx for k in ["sensor", "telemetry", "iot"]):
        return "Direct sensor telemetry and IoT gateways."
    if any(k in ctx for k in ["sql", "postgres", "mysql", "mssql", "sqlite", "warehouse", "bigquery", "snowflake"]):
        return "Manufacturing database or data warehouse (SQL-backed)."
    if any(k in ctx for k in ["csv", ".csv", "xlsx", "excel"]):
        return "File-based logs and exports (CSV/Excel) from plant systems."
    if "api" in ctx or "requests." in ctx:
        return "REST API from plant or MES systems."
    if "log" in ctx:
        return "Production execution logs."

    return "Operations data sources such as historians, SCADA/DCS tags, and production logs."

def _fill_comments_if_empty(text: str | None) -> str:
    text = (text or "").strip()
    if text:
        return text
    return "No additional comments or special considerations were provided for this KPI."

def generate_kpi_details(kpi_name: str, code_context: str) -> Dict[str, Any]:
    """Uses OpenAI's GPT model to generate plain text descriptions ONLY."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file.")

    client = OpenAI(api_key=api_key)

    # 1) Retrieval: domain KB + user overrides as few-shot guidance
    kb_examples = _retrieve_kb_examples(client, kpi_name, top_k=3)
    user_overrides = _load_user_overrides_for(kpi_name)

    kb_block = ""
    if kb_examples:
        # Provide compact JSON snippets as guidance (not mandatory)
        kb_block = "Domain Knowledge (Petrochemical KPI examples):\n" + json.dumps(kb_examples, ensure_ascii=False)

    overrides_block = ""
    if user_overrides:
        overrides_block = "User-Approved Overrides (preferred wording for this KPI):\n" + json.dumps(user_overrides, ensure_ascii=False)

    guidance = "\n\n".join([b for b in [kb_block, overrides_block] if b])

    prompt = f"""
    You are an expert technical writer for oil, gas, and petrochemicals.
    Use the KPI name, code, and any provided domain knowledge to write accurate, concise text.

    Guidance (optional, use if relevant):
    {guidance or "None"}

    RULES:
    1) Write each field as a natural-language sentence or brief paragraph (no bullets in raw text).
    2) Do NOT output lists, semicolons, or formulas (that's handled elsewhere).
    3) Stay specific to this KPI; do not copy irrelevant content from examples.

    KPI Name: "{kpi_name}"
    Code Context: ```python
    {code_context}
    ```

    Generate a JSON object with these exact keys:
    "description", "objective", "formula_description", "used_in_kpis",
    "input_measure", "unit_of_measure", "reporting_source", "comments".
    """

    retries = 8
    delay = 8
    result: Dict[str, Any] | None = None

    for i in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                temperature=0.1,
            )
            content = getattr(getattr(response, "choices", [None])[0], "message", None)
            content_text = getattr(content, "content", None)
            if not content_text or not isinstance(content_text, str):
                raise ValueError("Empty or invalid model response content.")
            parsed = json.loads(content_text)
            if not isinstance(parsed, dict):
                raise ValueError("Model response is not a JSON object.")
            result = parsed
            break
        except Exception:
            if i < retries - 1:
                time.sleep(delay)
                delay = min(delay * 2, 60)
                continue
            result = {
                "description": f"{kpi_name} is a key performance indicator used to assess process efficiency and operational performance.",
                "objective": f"The objective of {kpi_name} is to provide a clear measure that supports monitoring, decision making, and continuous improvement.",
                "formula_description": "Calculated directly from the inputs found in the code implementation.",
                "used_in_kpis": "This KPI can serve as an input to higher-level operational and performance dashboards.",
                "input_measure": "Derived from the variables used in the code calculation for this KPI.",
                "unit_of_measure": "See calculation and context for the most appropriate unit.",
                "reporting_source": "Typically sourced from process historians, production logs, or execution systems.",
                "comments": "No additional comments or special considerations were provided for this KPI."
            }

    # Ensure all required keys exist
    for key in ("description", "objective", "formula_description", "used_in_kpis",
                "input_measure", "unit_of_measure", "reporting_source", "comments"):
        result.setdefault(key, "")

    # Apply safeguards
    result["unit_of_measure"] = _infer_unit_of_measure(kpi_name, code_context, result.get("unit_of_measure"))
    result["reporting_source"] = _infer_reporting_source(code_context, result.get("reporting_source"))
    result["comments"] = _fill_comments_if_empty(result.get("comments"))

    # Domain enrichment (petrochemicals only, controlled by feature flag and strict classifier)
    result = _enrich_with_domain_hints(kpi_name, code_context, result)

    # Finally merge explicit user overrides (user takes precedence)
    if user_overrides:
        for k, v in user_overrides.items():
            if v:
                result[k] = v

    return result

# ... existing code ...

def generate_bluebook(source_code_path: str):
    """Main generator logic that yields progress messages."""
    # 1) Remove old generated .rst files (keep index.rst if present)
    for item in DOCS_SOURCE_DIR.glob('*.rst'):
        if item.is_file() and item.name != 'index.rst':
            item.unlink()
    yield "Cleaned old documentation files."

    # 2) Also remove previous HTML build so stale pages cannot survive
    build_dir = DOCS_SOURCE_DIR / '_build'
    if build_dir.exists():
        import shutil
        shutil.rmtree(build_dir, ignore_errors=True)
        yield "Removed previous Sphinx _build directory."

    # NEW: log the path we are scanning
    yield f"Scanning for KPIs in: {source_code_path}"

    kpis = find_kpis_in_directory(source_code_path)
    yield f"Scanner result: {len(kpis)} items"

    # Log first few KPIs for quick verification
    for idx, k in enumerate(kpis[:10], start=1):
        yield f"[{idx}] {k.get('name')} — {k.get('file_path')}:{k.get('file_line')}"

    if not kpis:
        yield "No KPIs found in the specified directory."
        return
    yield f"Found {len(kpis)} KPIs. Starting AI generation for descriptions..."