import math


def distance(p1, p2):
    return math.sqrt(
        (p1["x"] - p2["x"]) ** 2 +
        (p1["y"] - p2["y"]) ** 2
    )


def analyze_body(landmarks):

    LEFT_SHOULDER = 11
    RIGHT_SHOULDER = 12

    LEFT_HIP = 23
    RIGHT_HIP = 24

    NOSE = 0

    LEFT_ANKLE = 27
    RIGHT_ANKLE = 28

    shoulder_width = distance(
        landmarks[LEFT_SHOULDER],
        landmarks[RIGHT_SHOULDER]
    )

    hip_width = distance(
        landmarks[LEFT_HIP],
        landmarks[RIGHT_HIP]
    )

    body_height = (
        (
            landmarks[LEFT_ANKLE]["y"] +
            landmarks[RIGHT_ANKLE]["y"]
        ) / 2
    ) - landmarks[NOSE]["y"]

    shoulder_to_hip_ratio = shoulder_width / hip_width

    if shoulder_to_hip_ratio > 1.20:
        body_type = "Inverted Triangle"

    elif shoulder_to_hip_ratio > 1.05:
        body_type = "Athletic"

    elif shoulder_to_hip_ratio > 0.90:
        body_type = "Rectangle"

    else:
        body_type = "Pear"

    return {

        "body_height": round(body_height, 3),

        "shoulder_to_hip_ratio": round(
            shoulder_to_hip_ratio,
            3
        ),

        "body_type": body_type

    }