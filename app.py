import os
import threading
import json
from flask import Flask, render_template, request, jsonify, send_from_directory
from bluebook_generator.main import generate_bluebook
from bluebook_generator.kpi_extractor import find_kpis_in_directory
# Add these imports for deep scan
from bluebook_generator.kpi_extractor import _detect_language_by_extension as _dbg_detect_lang  # type: ignore

app = Flask(__name__)

BLUEBOOK_DIR = os.path.join(os.getcwd(), 'docs', '_build')
OVERRIDES_PATH = os.path.join(os.getcwd(), 'docs', 'overrides.json')

# --- Global state to track progress ---
status = {"running": False, "output": "Ready to start."}


def run_generation_in_background(path):
    """Wrapper to run our main logic and update status."""
    global status
    try:
        for message in generate_bluebook(path):
            status["output"] += f"\n{message}"
        status["output"] += "\n\n--- Bluebook Generation Complete! ---"
    except Exception as e:
        status["output"] += f"\n\nAn error occurred: {e}"
    finally:
        status["running"] = False


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_generation():
    """Start the bluebook generation process."""
    global status
    if status["running"]:
        return jsonify({"status": "Already running."}), 400

    path = request.form.get('path')
    if not path or not os.path.isdir(path):
        return jsonify({"status": "Invalid or missing folder path."}), 400

    status = {"running": True, "output": "Starting generation..."}

    thread = threading.Thread(target=run_generation_in_background, args=(path,))
    thread.start()

    return jsonify({"status": "Generation started."})


@app.route('/status')
def get_status():
    """Provide real-time status updates to the frontend."""
    return jsonify(status)


# --- ADD THIS NEW ROUTE ---
@app.route('/bluebook/<path:filename>')
def serve_bluebook(filename):
    """Serves the generated HTML files from the docs/_build directory."""
    return send_from_directory(BLUEBOOK_DIR, filename)


@app.route('/overrides/<kpi_name>', methods=['GET'])
def get_overrides(kpi_name):
    """Return saved overrides for a KPI (if any)."""
    try:
        if os.path.exists(OVERRIDES_PATH):
            with open(OVERRIDES_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return jsonify(data.get(kpi_name, {}))
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({})

@app.route('/overrides', methods=['POST'])
def save_overrides():
    """
    Body JSON:
    {
      "kpi_name": "Some KPI",
      "fields": {
        "description": "...",
        "objective": "...",
        "input_measure": "...",
        "unit_of_measure": "...",
        "reporting_source": "...",
        "comments": "..."
      }
    }
    """
    try:
        payload = request.get_json(force=True)
        kpi_name = payload.get("kpi_name")
        fields = payload.get("fields", {})
        if not kpi_name or not isinstance(fields, dict):
            return jsonify({"error": "Invalid payload"}), 400

        data = {}
        if os.path.exists(OVERRIDES_PATH):
            with open(OVERRIDES_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
        data.setdefault(kpi_name, {}).update({k: v for k, v in fields.items() if v is not None})

        os.makedirs(os.path.dirname(OVERRIDES_PATH), exist_ok=True)
        with open(OVERRIDES_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return jsonify({"status": "saved"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/edit')
def edit_page():
    """
    Simple edit page for a KPI. Usage: /edit?kpi=<KPI Name>
    This page loads existing overrides (if any) and lets the user save updates.
    """
    kpi_name = request.args.get("kpi", "").strip()
    if not kpi_name:
        kpi_name = ""
    return render_template("edit.html", kpi_name=kpi_name)

@app.route('/debug-scan')
def debug_scan():
    """
    Quick diagnostic: scan a folder and return the KPIs that would be found.
    Usage:
      /debug-scan?path=/absolute/path/to/folder
      /debug-scan?path=relative/path/from/cwd
    """
    raw = (request.args.get('path') or '').strip()
    if not raw:
        return jsonify({"error": "Provide a folder path via ?path="}), 400

    candidate = os.path.expanduser(raw)
    if not os.path.isabs(candidate):
        candidate = os.path.abspath(os.path.join(os.getcwd(), candidate))

    if not os.path.isdir(candidate):
        return jsonify({
            "error": "Folder not found",
            "received": raw,
            "resolved": candidate,
            "cwd": os.getcwd()
        }), 400

    # Run the scanner safely and handle any unexpected errors
    try:
        kpis = find_kpis_in_directory(candidate)
    except Exception as e:
        return jsonify({
            "error": "Scanner raised an exception",
            "resolved": candidate,
            "message": str(e)
        }), 500

    # Normalize None -> []
    if kpis is None:
        kpis = []

    return jsonify({
        "path": candidate,
        "count": len(kpis),
        "items": [
            {
                "name": k.get("name"),
                "file_path": k.get("file_path"),
                "file_line": k.get("file_line")
            } for k in kpis
        ]
    })

@app.route('/debug-scan-deep')
def debug_scan_deep():
    """
    Deep diagnostic: walk the folder, show every file, the language hint,
    and any KPIs detected per file. Uses public scanner to avoid internal helper errors.
    """
    raw = (request.args.get('path') or '').strip()
    if not raw:
        return jsonify({"error": "Provide a folder path via ?path="}), 400

    base = os.path.expanduser(raw)
    if not os.path.isabs(base):
        base = os.path.abspath(os.path.join(os.getcwd(), base))

    if not os.path.isdir(base):
        return jsonify({
            "error": "Folder not found",
            "received": raw,
            "resolved": base,
            "cwd": os.getcwd()
        }), 400

    # Run the public scanner once
    try:
        all_kpis = find_kpis_in_directory(base) or []
    except Exception as e:
        return jsonify({"error": "scanner-error", "message": str(e), "resolved": base}), 500

    # Index by file
    by_file = {}
    for k in all_kpis:
        fp = k.get("file_path")
        by_file.setdefault(fp, []).append(k)

    # Walk the directory to list every file, then attach KPIs from by_file
    per_file = []
    total_kpis = 0
    for dirpath, _, filenames in os.walk(base):
        for fn in filenames:
            path = os.path.join(dirpath, fn)
            p_lower = path.lower()
            lang = _dbg_detect_lang(p_lower)
            items = by_file.get(path, [])
            total_kpis += len(items)
            per_file.append({
                "file": path,
                "lang": lang,
                "kpi_count": len(items),
                "kpis": [{"name": i.get("name"), "line": i.get("file_line")} for i in items[:5]]
            })

    return jsonify({
        "path": base,
        "total_kpis": total_kpis,
        "files_scanned": len(per_file),
        "files": per_file
    })

if __name__ == '__main__':
    if not os.path.exists('docs/_build'):
        os.makedirs('docs/_build')
    app.run(debug=True)