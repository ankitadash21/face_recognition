from deepface import DeepFace
import cv2
import os

# Path to your faces folder
DB_PATH = "faces"

cam = cv2.VideoCapture(0)

print("Starting recognition... press Q to quit")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    try:
        result = DeepFace.find(img_path = frame, db_path = DB_PATH, enforce_detection=False, model_name="Facenet")
        if len(result) > 0 and len(result[0]) > 0:
            identity = result[0].iloc[0]['identity']
            name = os.path.splitext(os.path.basename(identity))[0]
        else:
            name = "Unknown"
    except:
        name = "Unknown"

    cv2.putText(frame, name, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Live Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
