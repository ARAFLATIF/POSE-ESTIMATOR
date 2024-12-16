import cv2
import mediapipe as mp
from pose_detector import PoseDetector
from exercise_counter import ExerciseCounter
from ui_overlay import UIOverlay
from config import CAMERA_ID, WINDOW_NAME

def main():
    cap = cv2.VideoCapture(CAMERA_ID)
    pose_detector = PoseDetector()
    exercise_counter = ExerciseCounter()
    ui_overlay = UIOverlay()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image, landmarks = pose_detector.detect_pose(frame)
        exercise_counter.update(landmarks)
        image = ui_overlay.draw(image, exercise_counter.get_stats(), landmarks)

        cv2.imshow(WINDOW_NAME, image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

