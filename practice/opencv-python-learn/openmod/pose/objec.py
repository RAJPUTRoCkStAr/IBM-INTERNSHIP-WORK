import mediapipe as mp
import cv2 as cv
mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron
cap = cv.VideoCapture(0)

with mp_objectron.Objectron(static_image_mode=False,
                            max_num_objects=5,
                            min_detection_confidence=0.5,
                            model_name='Bottle') as objectron:  # Change model_name as needed
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = objectron.process(frame)
        frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        if results.detected_objects:
            for detected_object in results.detected_objects:
                mp_drawing.draw_landmarks(
                    frame, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
                mp_drawing.draw_axis(frame, detected_object.rotation,
                                     detected_object.translation)
        cv.imshow('image', frame)
        if cv.waitKey(1) == ord('q'):
            break
cap.release()
cv.destroyAllWindows()
