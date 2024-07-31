import cv2 as cv
import mediapipe as mp 
import time
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
cap = cv.VideoCapture('med/1.mp4')
ptime = 0
while True:
    success , img  = cap.read()
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks) 
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape
            print(id,lm)
            cx,cy = int(lm.x*w),int(lm.y*h)
            cv.circle(img,(cx,cy),10,(250,0,0),cv.FILLED)




    img =cv.resize(img,(680,680))
    cTime = time.time()
    fps = 1/(cTime-ptime)
    ptime = cTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)
    cv.imshow("imgae",img)
    if cv.waitKey(1) == ord('q'):
        break