from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "KRVE CORE ENGINE LIVE 🚀"

@app.route("/upload", methods=["POST"])
def upload():

    try:
        file = request.files.get("file")

        if file is None:
            return jsonify({"error": "No file received"}), 400

        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        return jsonify({
            "modelUrl": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
            "chest": "38.5 IN",
            "waist": "31.5 IN",
            "hip": "40.2 IN",
            "size": "KRVE MATCH M"
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": "server crash"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)