import cv2
from hand_star.hand_star import HandStar

def main():
    cap = cv2.VideoCapture(0)
    detector = HandStar(maxHands=2)

    while True:
        success, img = cap.read()
        if not success:
            break
        
        img = detector.detect_hands(img)
        lmList = detector.get_hand_positions(img)
        
        # Additional functionalities
        fingersList = detector.get_fingers_status()
        for i, fingers in enumerate(fingersList):
            print(f"Hand {i+1}:", fingers)
            length, img, lineInfo = detector.calculate_distance(4, 8, img, handNo=i)
            print(f"Hand {i+1} Distance:", length)
        
        cv2.imshow('Hand Detection', img)
        
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()