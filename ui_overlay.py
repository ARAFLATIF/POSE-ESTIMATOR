import cv2
import numpy as np

class UIOverlay:
    def draw(self, image, stats, landmarks):
        cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
        cv2.putText(image, 'REPS', (15,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(stats['counter']), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        cv2.putText(image, 'STAGE', (65,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, stats['stage'], (60,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

        if landmarks is not None:
            elbow = tuple(np.multiply(landmarks[13][:2], [image.shape[1], image.shape[0]]).astype(int))
            cv2.putText(image, f"Angle: {stats.get('angle', 'N/A')}", 
                        elbow, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)

        return image
