import math


LEFT_SHOULDER = 11
RIGHT_SHOULDER = 12
LEFT_HIP = 23
RIGHT_HIP = 24


def distance(p1, p2):
    return math.sqrt(
        (p1["x"] - p2["x"]) ** 2 +
        (p1["y"] - p2["y"]) ** 2
    )


def get_cloth_alignment(landmarks):

    left_shoulder = landmarks[LEFT_SHOULDER]
    right_shoulder = landmarks[RIGHT_SHOULDER]

    left_hip = landmarks[LEFT_HIP]
    right_hip = landmarks[RIGHT_HIP]

    shoulder_width = distance(
        left_shoulder,
        right_shoulder
    )

    hip_width = distance(
        left_hip,
        right_hip
    )

    shirt_width = shoulder_width * 1.40

    shirt_height = distance(
        {
            "x": (left_shoulder["x"] + right_shoulder["x"]) / 2,
            "y": (left_shoulder["y"] + right_shoulder["y"]) / 2
        },
        {
            "x": (left_hip["x"] + right_hip["x"]) / 2,
            "y": (left_hip["y"] + right_hip["y"]) / 2
        }
    ) * 1.35

    center_x = (
        left_shoulder["x"] +
        right_shoulder["x"]
    ) / 2

    center_y = (
        left_shoulder["y"] +
        right_shoulder["y"]
    ) / 2 + (shirt_height * 0.35)

    return {

        "shirt_center_x": round(center_x, 4),

        "shirt_center_y": round(center_y, 4),

        "shirt_width": round(shirt_width, 4),

        "shirt_height": round(shirt_height, 4),

        "shoulder_width": round(shoulder_width, 4),

        "hip_width": round(hip_width, 4)

    }