import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

MODEL_PATH = "models/pose_landmarker_lite.task"

BaseOptions = python.BaseOptions
PoseLandmarker = vision.PoseLandmarker
PoseLandmarkerOptions = vision.PoseLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=VisionRunningMode.IMAGE,
    output_segmentation_masks=False
)

detector = PoseLandmarker.create_from_options(options)


def detect_pose(image_path):

    image = mp.Image.create_from_file(image_path)

    result = detector.detect(image)

    if len(result.pose_landmarks) == 0:
        return None

    landmarks = []

    for lm in result.pose_landmarks[0]:

        landmarks.append({

            "x": lm.x,

            "y": lm.y,

            "z": lm.z,

            "visibility": lm.visibility

        })

    return landmarks