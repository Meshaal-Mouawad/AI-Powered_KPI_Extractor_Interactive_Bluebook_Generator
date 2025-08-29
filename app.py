import os
import threading
from flask import Flask, render_template, request, jsonify, send_from_directory
from bluebook_generator.main import generate_bluebook

app = Flask(__name__)

# --- Path to the generated HTML files ---
BLUEBOOK_DIR = os.path.join(os.getcwd(), 'docs', '_build')

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


if __name__ == '__main__':
    if not os.path.exists('docs/_build'):
        os.makedirs('docs/_build')
    app.run(debug=True)