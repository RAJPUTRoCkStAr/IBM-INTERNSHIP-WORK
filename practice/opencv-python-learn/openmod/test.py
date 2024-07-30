import cv2 as cv
from openmod.FaceDetection import FaceDetector
cap = cv.VideoCapture(0)
detector = FaceDetector(max_faces=2)
while True:
    success, img = cap.read()
    if not success:
        break
    img, faces = detector.find_face_mesh(img, meshdraw=True,pointdraw=True)
    cv.imshow('Image', img)
    
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
