import cv2 as cv
import mediapipe as mp
from facedetmod import FaceDetector
from Plot import LivePlot 

cap = cv.VideoCapture(0)
detector = FaceDetector(max_faces=1)
plotY = LivePlot(640,360,[20,50])
idList = [22,23,24,26,110,157,158,159,160,161,130,243]
ratioList  =[]
blinkcounter = 0
counter = 0
while True:
    success , img = cap.read()
    img,faces = detector.find_face_mesh(img,draw=False)
    if faces:
        face = faces[0]
        for id in idList:
            cv.circle(img,face[id],5,(255,0,255),cv.FILLED)
        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]
        lengthVer ,_ = detector.findDistance(leftUp,leftDown)
        lengthhor ,_ = detector.findDistance(leftLeft,leftRight)
        cv.line(img,leftUp,leftDown,(0,250,10),3)
        cv.line(img,leftLeft,leftRight,(0,250,10),3)
        ratio = (lengthVer/lengthhor)*100
        ratioList.append(ratio)
        if len(ratioList) > 3:
            ratioList.pop(0)
        ratioAvg = sum(ratioList)/len(ratioList)
        if ratioAvg < 35 and counter == 0:
            blinkcounter +=1
            counter = 1
        if counter != 0:
            counter +=1 
            if counter > 10:
                counter = 0
        cv.putText(img, f'blink counter : {blinkcounter}',(100,100) ,cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 250), 2)
        imgPlot = plotY.update(ratioAvg)
        cv.imshow('ImagePlot',imgPlot)
    cv.imshow('image',img)
    if cv.waitKey(1) == ord('q'):
            break