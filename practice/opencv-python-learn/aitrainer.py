import cv2 as cv
import numpy as np
import time
from PoseModule import PoseDetector
cap = cv.VideoCapture(0)

detector = PoseDetector(flip=False)
count = 0
dir = 0
pTime = 0
while True:
    success,img = cap.read()
    # img = cv.imread('med/images.jpeg')
    # img = cv.resize(img,(1280,720))
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img,False)
    # print(lmList)
    #left arm
    angle = detector.findAngle(img,11,13,15)
    per = np.interp(angle,(195,290),(0,100))
    # print(f"this is angle{angle}: this is percentage {per}")
    if per == 100:
        if dir ==0:
            count += 0.5
            dir = 1
    if per == 0:
        if dir ==1:
            count += 0.5
            dir = 0
    # print(count)
    # cv.putText(img,str(count),(50,100),cv.FONT_HERSHEY_DUPLEX,2,(255,0,255),2) #this way you can calculate if its half also
    cv.putText(img,str(int(count)),(150,100),cv.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}', (10, 70), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    cv.imshow('image',img)
    if cv.waitKey(1) == ord('q'):
        break