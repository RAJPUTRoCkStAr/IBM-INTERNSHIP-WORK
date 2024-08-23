from KAZIER import HandStar
import cv2

cap = cv2.VideoCapture(0)
detector = HandStar(maxHands=2)
while True:
    success, img = cap.read()
    if not success:
        break
    img = detector.detect_hands(img)
    lmList = detector.get_hand_positions(img)
    if len(lmList) != 0:
        fingersList = detector.get_fingers_status()
        handFingers = fingersList[0]
        if handFingers[0] == 0 and handFingers[1] == 0 and handFingers[2] == 1:
            print("three")
        if handFingers[0] == 0 and handFingers[1] == 0 and handFingers[2] == 0 and handFingers[3] ==1 and handFingers[4] ==1:
            print("two")
    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()