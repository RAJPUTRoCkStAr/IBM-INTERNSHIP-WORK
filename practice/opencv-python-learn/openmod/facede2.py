import cv2 as cv
import mediapipe as mp
import time

cap =cv.VideoCapture(0)
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=2,circle_radius=2)
while True:
    success , img= cap.read()
    imgRgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = faceMesh.process(imgRgb)
    if results.multi_face_landmarks:
          for faceLms in results.multi_face_landmarks:
                mpDraw.draw_landmarks(img,faceLms,mpFaceMesh.FACEMESH_CONTOURS,
                                      drawSpec,drawSpec)
                for id,lm in enumerate(faceLms.landmark):
                    # print(lm)
                    ih,iw,ic = img.shape
                    x,y = int(lm.x*iw),int(lm.y*ih)
                    print(id,x,y)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)
    cv.imshow("image",img)
    if cv.waitKey(1) == ord('q'):
            break
