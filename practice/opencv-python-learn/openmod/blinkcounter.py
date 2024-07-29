import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)

while True:
    success , img = cap.read()
    img = cv.resize(img,(640,360))
    cv.imshow('image',img)
    if cv.waitKey(1) == ord('q'):
            break