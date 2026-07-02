from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from backend.pose_detector import detect_pose
from backend.measurement import calculate_measurements
from backend.body_analyzer import analyze_body
from backend.height_estimator import estimate_height

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return "KRVE AI SERVER RUNNING 🚀"


@app.route("/api/pose", methods=["POST"])
def pose():

    if "image" not in request.files:
        return jsonify({
            "status": "error",
            "message": "No image uploaded"
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "status": "error",
            "message": "No file selected"
        }), 400

    image_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(image_path)

    try:

        landmarks = detect_pose(image_path)

        if landmarks is None:
            return jsonify({
                "status": "error",
                "message": "No person detected"
            })

        measurements = calculate_measurements(landmarks)

        body_analysis = analyze_body(landmarks)

        height = estimate_height(landmarks)

        return jsonify({

            "status": "success",

            "total_landmarks": len(landmarks),

            "measurements": measurements,

            "body_analysis": body_analysis,

            "height": height,

            "landmarks": landmarks

        })

    except Exception as e:

        return jsonify({

            "status": "error",

            "message": str(e)

        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )