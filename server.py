from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "SECRET SERVER", 200

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, "received_log.enc")
        file.save(filepath)
        return "File received!", 200
    return "No file received!", 400

@app.route("/upload", methods=["GET"])
def upload_get():
    return "Send a POST request with a file to this endpoint.", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)