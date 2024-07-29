import cv2
import time
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from hand_star.hand_star import HandStar
cw, ch = 720, 540
cap = cv2.VideoCapture(0)
cap.set(3, cw)
cap.set(4, ch)
detector = HandStar(detectioncon=0.7)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
min_volume = -45
max_volume = 0
volbar = 400
pTime = 0
while True:
    success, img = cap.read()
    if not success:
        break
    img = detector.detect_hands(img)
    lmList = detector.get_hand_positions(img)
    if len(lmList) > 0:
        length, img, lineInfo = detector.calculate_distance(4, 8, img)
        cx, cy = lineInfo[4], lineInfo[5] 
        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 200, 0), cv2.FILLED)
        vol = np.interp(length, [50, 300], [min_volume, max_volume])
        volbar = np.interp(length, [50, 300], [400, 150])
        print(int(length), vol)
        try:
            volume.SetMasterVolumeLevel(vol, None)
        except Exception as e:
            print(f"Error setting volume: {e}")
        cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
        cv2.rectangle(img, (50, int(volbar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
