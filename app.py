from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import cv2
import mediapipe as mp

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)

@app.route("/")
def home():
    return "KRVE AI PHASE 4 VISION ENGINE 🚀"

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("file")
    height = int(request.form.get("height", 170))

    if not file:
        return jsonify({"error": "No file"}), 400

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    # 🧠 READ IMAGE
    image = cv2.imread(path)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    result = pose.process(rgb)

    # default fallback values
    shoulder = height * 0.25
    chest = height * 0.50
    waist = height * 0.44
    hip = height * 0.53

    # 🧠 REAL LANDMARK DETECTION (if detected)
    if result.pose_landmarks:
        landmarks = result.pose_landmarks.landmark

        left_shoulder = landmarks[11]
        right_shoulder = landmarks[12]
        left_hip = landmarks[23]
        right_hip = landmarks[24]

        # simple normalized conversion
        shoulder = abs(left_shoulder.x - right_shoulder.x) * height * 100
        hip = abs(left_hip.x - right_hip.x) * height * 100
        waist = hip * 0.85
        chest = shoulder * 1.1

    # size logic
    if waist < 75:
        size = "S"
    elif waist < 85:
        size = "M"
    elif waist < 95:
        size = "L"
    else:
        size = "XL"

    return jsonify({
        "modelUrl": "https://modelviewer.dev/shared-assets/models/NeilArmstrong.glb",
        "shoulder": f"{round(shoulder,1)} cm",
        "chest": f"{round(chest,1)} cm",
        "waist": f"{round(waist,1)} cm",
        "hip": f"{round(hip,1)} cm",
        "size": size,
        "engine": "KRVE PHASE 4 AI VISION"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)