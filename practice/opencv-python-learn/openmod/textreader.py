import cv2 as cv
import mediapipe as mp
from openmod.FaceDetection import FaceDetector
import numpy as np
cap = cv.VideoCapture(0)
detector = FaceDetector(max_faces=1)
TextList = [
    "Java: 'Where's my semicolon?'",
    "Python: 'I don't need one!'",
   "Java: 'Why so many boilerplate lines?'",
    "Python: 'Less code, more fun!'",
    "Java: 'Error messages are cryptic.'",
    "Python: 'Error messages are friendly.'",
    "Java: 'More classes, more confusion.'",
    "Python: 'Fewer classes, clear code.'",
]
sen = 10 #more is less
while True:
    success, img = cap.read()
    imgText = np.zeros_like(img)
    if not success:
        break
    img,faces = detector.find_face_mesh(img,False,False)
    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        w,_ = detector.findDistance(pointLeft,pointRight)
        W = 6.3 
        f = 560
        d = (W*f)/w
        cv.putText  (img,f'Depth : {int(d)} cm ',
                    (face[10][0]-150,face[10][1]-100),
                    cv.FONT_HERSHEY_SIMPLEX,
                    1.3, (255, 0, 0), 5)
        for i,text in enumerate(TextList):
            SingleHeight = 20 + int((int(d/sen)*sen)/4)
            scale = 0.4 + int(d/sen)*sen/75
            cv.putText(imgText,text,(50,50+(i*SingleHeight)),cv.FONT_ITALIC,scale,(0,255,0),2)
    merge_img = np.hstack((img,imgText))
    cv.imshow('Text Reader', merge_img)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
