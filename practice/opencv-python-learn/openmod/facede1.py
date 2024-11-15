import cv2
import mediapipe as mp 
import time 
cap = cv2.VideoCapture(0)
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
FaceDetection = mpFaceDetection.FaceDetection()
pTime = 0
while True:
    success,img = cap.read()
    # img = cv2.flip(img,1)
    imgRgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = FaceDetection.process(imgRgb)
    # print(results)
    if results.detections:
        for id,detection in enumerate(results.detections):
            # mpDraw.draw_detection(img,detection)
            # print(id,detection)
            bboxC  = detection.location_data.relative_bounding_box
            ih,iw,ic = img.shape
            bbox = int(bboxC.xmin * iw),int(bboxC.ymin * ih),\
                int(bboxC.width * iw),int(bboxC.height * ih)
            cv2.rectangle(img,bbox,(255,0,0),2)
            cv2.putText(img, f'{int(detection.score[0]*100)}', (bbox[0],bbox[1]-20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 250), 2)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)
    cv2.imshow('Image',img)
    if cv2.waitKey(1) == ord('q'):
        break
