import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    img = cv.line(frame,(0,height),(width,0),(0,255,0),5)
    img = cv.line(frame,(0,0),(width,height),(0,0,255),5)


    cv.imshow('videocapture',img)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()