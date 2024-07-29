# import cv2 as cv
# import mediapipe as mp
# from facedetmod import FaceDetector

# # Initialize Face Detector
# cap = cv.VideoCapture(0)
# detector = FaceDetector(max_faces=1)

# # Define landmark points for different facial features
# facial_landmarks = {
#     'left_eye': [33, 133, 160, 159, 158, 157, 173, 153, 144, 163, 7, 246, 161, 160, 159, 158],
#     'right_eye': [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398],
#     'left_eyebrow': [70, 63, 105, 66, 107, 55, 193],
#     'right_eyebrow': [336, 296, 334, 293, 300, 276, 283],
#     'nose': [1, 2, 5, 195, 4, 275, 274, 278, 279, 280, 295, 294, 369, 363],
#     'mouth': [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88],
#     'jaw': [10, 109, 67, 103, 54, 21, 162, 127, 234, 93, 132, 58, 172, 136, 150, 176, 148, 152, 377, 400, 378, 379, 397, 288]
# }

# # Colors for each part
# colors = {
#     'left_eye': (0, 255, 0),
#     'right_eye': (255, 0, 0),
#     'left_eyebrow': (0, 255, 255),
#     'right_eyebrow': (255, 255, 0),
#     'nose': (255, 0, 255),
#     'mouth': (0, 0, 255),
#     'jaw': (128, 0, 128)
# }

# while True:
#     success, img = cap.read()
#     if not success:
#         break
    
#     img, faces = detector.find_face_mesh(img, draw=False)
#     if faces:
#         face = faces[0]
        
#         for part, points in facial_landmarks.items():
#             for point in points:
#                 cv.circle(img, face[point], 3, colors[part], cv.FILLED)
#                 cv.putText(img, str(point), face[point], cv.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
    
#     cv.imshow('Image', img)
    
#     if cv.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()
import cv2 as cv
import mediapipe as mp
from facedetmod import FaceDetector

# Initialize Face Detector
cap = cv.VideoCapture(0)
detector = FaceDetector(max_faces=1)

# Define landmark points for different facial features
facial_landmarks = {
    'left_eye': [33, 133, 160, 159, 158, 157, 173, 153, 144, 163, 7, 246, 161, 160, 159, 158],
    'right_eye': [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398],
    'left_eyebrow': [70, 63, 105, 66, 107, 55, 193],
    'right_eyebrow': [336, 296, 334, 293, 300, 276, 283],
    'nose':#left 
    [1, 2, 5, 98, 97, 2, 327, 326, 325, 91, 128, 209, 198, 217, 67, 112, 246, 191],
    #right side 
    # [1, 2, 5, 195, 4, 275, 285, 274, 278, 280, 331, 294, 455, 399, 419, 456, 363, 464, 395, 369],
    'mouth': [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88],
    'jaw': [10, 109, 67, 103, 54, 21, 162, 127, 234, 93, 132, 58, 172, 136, 150, 176, 148, 152, 377, 400, 378, 379, 397, 288],
    'forehead': [10, 338, 297, 332, 284, 251, 389, 361, 454, 323, 361, 355, 368, 264, 447, 386, 374, 373]
}

# Colors for each part
colors = {
    'left_eye': (0, 255, 0),
    'right_eye': (255, 0, 0),
    'left_eyebrow': (0, 255, 255),
    'right_eyebrow': (255, 255, 0),
    'nose': (255, 0, 255),
    'mouth': (0, 0, 255),
    'jaw': (128, 0, 128),
    'forehead': (0, 128, 255)
}

while True:
    success, img = cap.read()
    if not success:
        break
    
    img, faces = detector.find_face_mesh(img, draw=False)
    if faces:
        face = faces[0]
        
        for part, points in facial_landmarks.items():
            for point in points:
                cv.circle(img, face[point], 3, colors[part], cv.FILLED)
                cv.putText(img, str(point), face[point], cv.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
    
    cv.imshow('Image', img)
    
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


