import cv2
import time
import numpy as np
import own_model.handtrack as ht
import math
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#############
cw ,ch = 720, 540

#############


cap = cv2.VideoCapture(0)
cap.set(3,cw)
cap.set(4,ch)
pTime=0
detector = ht.HandDetector(detectioncon=0.7)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = interface.QueryInterface(IAudioEndpointVolume)
volume = cast(interface,POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
# volume.GetVolumeRange()

min_volume = -45
max_volume = 0
volbar = 400
while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmLiist = detector.findPosition(img)
    if len(lmLiist) !=0:
        # print(lmLiist[4],lmLiist[8])
        x1,y1 = lmLiist[4][1],lmLiist[4][2]
        x2,y2 = lmLiist[8][1],lmLiist[8][2]
        cx,cy = (x1+x2)//2,(y1+y2)//2
        cv2.circle(img,(x1,y1),15,(0,155,155),cv2.FILLED)
        cv2.circle(img,(x2,y2),15,(0,155,155),cv2.FILLED)
        cv2.circle(img,(cx,cy),15,(0,155,155),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(0,155,155),3)
        length = math.hypot(x2-x1,y2-y1)
        # print(length)
        if length < 50:
            cv2.circle(img,(cx,cy),15,(0,200,0),cv2.FILLED)
        vol = np.interp(length,[50,300],[min_volume,max_volume])
        volbar = np.interp(length,[50,300],[400,150])
        print(int(length),vol)
        try:
            volume.SetMasterVolumeLevel(vol, None)
        except Exception as e:
            print(f"Error setting volume: {e}")
        cv2.rectangle(img,(50,150),(85,400),(255,0,0),3)
        cv2.rectangle(img,(50,int(volbar)),(85,400),(255,0,0),cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)

    cv2.imshow('main page', img)
    if cv2.waitKey(1) == ord('q'):
        break