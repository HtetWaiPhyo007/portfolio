import cv2
import os
from deepface import DeepFace
import numpy as np

# Load known face
known_face_path = os.path.join(os.path.dirname(__file__), "known_faces", "htet.jpg")
known_name = "Htet Wai Phyo"

# Precompute embedding
print("🧠 Loading known face...")
try:
    known_embedding = DeepFace.represent(
        img_path=known_face_path, model_name="VGG-Face", enforce_detection=True
    )[0]['embedding']
    print("✅ Known face loaded")
except Exception as e:
    print(f"❌ Failed to load known face: {e}")
    exit()

# Start webcam
video_capture = cv2.VideoCapture(0)
print("🎥 Camera started... Press Q to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        continue

    try:
        # Save current frame temporarily
        temp_frame_path = "temp_frame.jpg"
        cv2.imwrite(temp_frame_path, frame)

        # Get embedding of current face
        embeddings = DeepFace.represent(
            img_path=temp_frame_path, model_name="VGG-Face", enforce_detection=False
        )

        for item in embeddings:
            embedding = item['embedding']
            distance = np.linalg.norm(np.array(embedding) - np.array(known_embedding))
            threshold = 0.6

            if distance < threshold:
                # Draw name
                cv2.putText(frame, known_name, (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.rectangle(frame, (20, 20), (300, 100), (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Unknown", (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.rectangle(frame, (20, 20), (300, 100), (0, 0, 255), 2)

    except Exception as e:
        print("⚠️", e)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
