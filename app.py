from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "KRVE AI Backend is Live 🚀"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    return jsonify({
        "modelUrl": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
        "chest": "92 cm",
        "waist": "78 cm",
        "hip": "94 cm",
        "size": "M"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)