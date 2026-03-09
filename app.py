from flask import Flask, render_template, request, jsonify
import subprocess
import os
import sys
import json

app = Flask(__name__)

# Paths
BASE_DIR = os.path.dirname(__file__)
PROCESS_SCRIPT = os.path.join(BASE_DIR, "process_incoming.py")
RESPONSE_FILE = os.path.join(BASE_DIR, "response.txt")
CHUNKS_FILE = os.path.join(BASE_DIR, "relevant_chunks.json")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    user_query = data.get("question", "").strip()

    if not user_query:
        return jsonify({"error": "Please enter a question"}), 400

    try:
        # Run process_incoming.py with the user query
        result = subprocess.run(
            [sys.executable, PROCESS_SCRIPT, user_query],
            capture_output=True,
            text=True,
            check=True
        )

        # Read the response
        response_text = ""
        relevant_chunks = []

        if os.path.exists(RESPONSE_FILE):
            with open(RESPONSE_FILE, "r", encoding="utf-8") as f:
                response_text = f.read().strip()

        # Read relevant chunks if available
        if os.path.exists(CHUNKS_FILE):
            with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
                relevant_chunks = json.load(f)

        return jsonify({
            "answer": response_text,
            "chunks": relevant_chunks
        })

    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Error processing your question: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
