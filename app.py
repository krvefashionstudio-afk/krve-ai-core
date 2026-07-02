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
    return "KRVE AI VIRTUAL TRY-ON ENGINE LIVE 🚀"

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("file")
    height = int(request.form.get("height", 170))

    if not file:
        return jsonify({"error": "No image"}), 400

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    # 🧠 PHASE 3: SIMULATED AI LANDMARK ENGINE
    shoulder = round(height * 0.25 + random.uniform(-2, 2), 1)
    chest = round(height * 0.52 + random.uniform(-3, 3), 1)
    waist = round(height * 0.44 + random.uniform(-3, 3), 1)
    hip = round(height * 0.54 + random.uniform(-3, 3), 1)

    # body type detection
    ratio = waist / height

    if ratio < 0.43:
        body_type = "Slim Fit"
    elif ratio < 0.47:
        body_type = "Athletic Fit"
    else:
        body_type = "Regular Fit"

    return jsonify({
        "modelUrl": "https://modelviewer.dev/shared-assets/models/NeilArmstrong.glb",
        "shoulder": f"{shoulder} cm",
        "chest": f"{chest} cm",
        "waist": f"{waist} cm",
        "hip": f"{hip} cm",
        "bodyType": body_type,
        "size": "KRVE FIT " + ("S" if waist < 75 else "M" if waist < 85 else "L"),
        "engine": "PHASE 3 AI VIRTUAL FIT"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    