from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "KRVE AI Backend is Live 🚀"

# IMAGE UPLOAD API
@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file found"}), 400

    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    return jsonify({
        "message": "Image uploaded successfully",
        "file_path": path
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)