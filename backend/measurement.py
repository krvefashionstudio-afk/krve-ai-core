import math


def distance(p1, p2):
    return math.sqrt(
        (p1["x"] - p2["x"]) ** 2 +
        (p1["y"] - p2["y"]) ** 2
    )


def calculate_measurements(landmarks):

    LEFT_SHOULDER = 11
    RIGHT_SHOULDER = 12

    LEFT_HIP = 23
    RIGHT_HIP = 24

    LEFT_ELBOW = 13
    LEFT_WRIST = 15

    LEFT_KNEE = 25
    LEFT_ANKLE = 27

    shoulder_width = distance(
        landmarks[LEFT_SHOULDER],
        landmarks[RIGHT_SHOULDER]
    )

    hip_width = distance(
        landmarks[LEFT_HIP],
        landmarks[RIGHT_HIP]
    )

    arm_length = (
        distance(
            landmarks[LEFT_SHOULDER],
            landmarks[LEFT_ELBOW]
        )
        +
        distance(
            landmarks[LEFT_ELBOW],
            landmarks[LEFT_WRIST]
        )
    )

    leg_length = (
        distance(
            landmarks[LEFT_HIP],
            landmarks[LEFT_KNEE]
        )
        +
        distance(
            landmarks[LEFT_KNEE],
            landmarks[LEFT_ANKLE]
        )
    )

    return {

        "shoulder_width": shoulder_width,

        "hip_width": hip_width,

        "arm_length": arm_length,

        "leg_length": leg_length

    }