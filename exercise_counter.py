from angle_calculator import calculate_angle
from config import ELBOW_ANGLE_THRESHOLD

class ExerciseCounter:
    def __init__(self):
        self.counter = 0
        self.stage = None
        self.prev_angle = None

    def update(self, landmarks):
        if landmarks is None:
            return

        shoulder = landmarks[11][:2]
        elbow = landmarks[13][:2]
        wrist = landmarks[15][:2]

        angle = calculate_angle(shoulder, elbow, wrist)

        if self.prev_angle is None:
            self.prev_angle = angle

        if angle > ELBOW_ANGLE_THRESHOLD and self.prev_angle <= ELBOW_ANGLE_THRESHOLD:
            self.stage = "down"
        elif angle < ELBOW_ANGLE_THRESHOLD and self.prev_angle >= ELBOW_ANGLE_THRESHOLD and self.stage == "down":
            self.stage = "up"
            self.counter += 1

        self.prev_angle = angle

    def get_stats(self):
        return {
            "counter": self.counter,
            "stage": self.stage
        }
