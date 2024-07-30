import cv2 as cv
import mediapipe as mp
from openmod.FaceDetection import FaceDetector
cap = cv.VideoCapture(0)
detector = FaceDetector(max_faces=1)
while True:
    success, img = cap.read()
    if not success:
        break
    img,faces = detector.find_face_mesh(img,False,False)
    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        #drawing
        # cv.circle(img,pointLeft,5,(255,0,255),cv.FILLED)
        # cv.circle(img,pointRight,5,(255,0,255),cv.FILLED)
        # cv.line(img,pointLeft,pointRight,(0,255,0),3)
        w,_ = detector.findDistance(pointLeft,pointRight)
        W = 6.3 
        # d = 50
        # f = (w*d)/W
        # print(f)
        f = 560
        d = (W*f)/w
        # print(w)
        # print(d)
        cv.putText(img,f'Depth : {int(d)} cm ',
                   (face[10][0]-150,face[10][1]-100),
                   cv.FONT_HERSHEY_SIMPLEX,
                1.3, (255, 0, 0), 5)

    cv.imshow('Image', img)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
