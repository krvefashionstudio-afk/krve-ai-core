import math


def distance(p1, p2):
    return math.sqrt(
        (p1["x"] - p2["x"]) ** 2 +
        (p1["y"] - p2["y"]) ** 2
    )


def estimate_height(landmarks):

    NOSE = 0
    LEFT_ANKLE = 27
    RIGHT_ANKLE = 28

    ankle_y = (
        landmarks[LEFT_ANKLE]["y"] +
        landmarks[RIGHT_ANKLE]["y"]
    ) / 2

    body_height = abs(
        ankle_y - landmarks[NOSE]["y"]
    )

    return {

        "normalized_height": round(body_height, 3),

        "confidence": 1.0

    }