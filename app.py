from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "KRVE AI BODY SCANNER LIVE 🚀"

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("file")
    height = request.form.get("height", 170)

    if not file:
        return jsonify({"error": "No image uploaded"}), 400

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    # 🧠 MOCK AI BODY ANALYSIS (PHASE 2 LOGIC)

    h = int(height)

    # fake AI logic based on height randomness
    chest = round((h * 0.52) + random.uniform(-3, 3), 1)
    waist = round((h * 0.44) + random.uniform(-3, 3), 1)
    hip = round((h * 0.54) + random.uniform(-3, 3), 1)

    # size prediction logic
    if waist < 70:
        size = "S"
    elif waist < 80:
        size = "M"
    elif waist < 90:
        size = "L"
    else:
        size = "XL"

    return jsonify({
        "modelUrl": "https://modelviewer.dev/shared-assets/models/NeilArmstrong.glb",
        "chest": f"{chest} cm",
        "waist": f"{waist} cm",
        "hip": f"{hip} cm",
        "size": size,
        "engine": "KRVE AI PHASE 2"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)