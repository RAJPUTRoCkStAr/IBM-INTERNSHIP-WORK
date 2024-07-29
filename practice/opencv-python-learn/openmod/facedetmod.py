import cv2
import mediapipe as mp
import time

class FaceDetector:
    def __init__(self, min_detection_confidence=0.5, static_mode=False, max_faces=2, min_tracking_confidence=0.5):
        self.min_detection_confidence = min_detection_confidence
        self.static_mode = static_mode
        self.max_faces = max_faces
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(min_detection_confidence=self.min_detection_confidence)
        
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(static_image_mode=self.static_mode, 
                                                    max_num_faces=self.max_faces, 
                                                    min_detection_confidence=self.min_detection_confidence, 
                                                    min_tracking_confidence=self.min_tracking_confidence)
        self.draw_spec = self.mp_draw.DrawingSpec(thickness=2, circle_radius=2)

    def find_faces(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.face_detection.process(img_rgb)
        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])
                if draw:
                    img = self.imp_draw(img, bbox)
                    cv2.putText(img, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 250), 2)
        return img, bboxs

    def imp_draw(self, img, bbox, l=30, t=10, rt=1):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h
        cv2.rectangle(img, bbox, (255, 0, 0), rt)
        # Top left
        cv2.line(img, (x, y), (x + l, y), (255, 255, 0), 2)
        cv2.line(img, (x, y), (x, y + l), (255, 255, 0), 2)
        # Top right
        cv2.line(img, (x1, y), (x1 - l, y), (255, 255, 0), 2)
        cv2.line(img, (x1, y), (x1, y + l), (255, 255, 0), 2)
        # Bottom left
        cv2.line(img, (x, y1), (x + l, y1), (255, 255, 0), 2)
        cv2.line(img, (x, y1), (x, y1 - l), (255, 255, 0), 2)
        # Bottom right
        cv2.line(img, (x1, y1), (x1 - l, y1), (255, 255, 0), 2)
        cv2.line(img, (x1, y1), (x1, y1 - l), (255, 255, 0), 2)
        return img

    def find_face_mesh(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.face_mesh.process(img_rgb)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, faceLms, self.mp_face_mesh.FACEMESH_CONTOURS,
                                           self.draw_spec, self.draw_spec)
                face = []
                for id, lm in enumerate(faceLms.landmark):
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    # cv2.putText(img, str(id),(x,y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 1)
                    # print(id, x, y)
                    face.append([x, y])
                faces.append(face)
        return img, faces

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = FaceDetector()
    while True:
        success, img = cap.read()
        if not success:
            break
        img = cv2.flip(img, 1)
         # img, bboxs = detector.FindFaces(img)
        # print(bboxs) 
        img, faces = detector.find_face_mesh(img)
        if len(faces) != 0:
            print(f"Number of faces detected: {len(faces)}")
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
