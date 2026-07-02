from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "KRVE HUMAN ENGINE LIVE 🚀"

@app.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files.get("file")

        if not file:
            return jsonify({"error": "No file"}), 400

        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        # 🧠 MOCK HUMAN BODY ENGINE
        return jsonify({
            "modelUrl": "https://modelviewer.dev/shared-assets/models/NeilArmstrong.glb",
            "chest": "94 cm",
            "waist": "78 cm",
            "hip": "96 cm",
            "size": "KRVE FIT M",
            "type": "human-avatar"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)