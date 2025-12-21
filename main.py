import cv2
import mediapipe as mp
import math
import winsound

# ----------------------------- #
# Auxiliary Functions
# ----------------------------- #

# Calculate the Euclidean distance between two points
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

# Calculate Eye Aspect Ratio (EAR)
def calc_EAR(landmarks, eye_indices):
    p1, p2, p3, p4, p5, p6 = [landmarks[i] for i in eye_indices]

    vertical1 = dist(p2, p6)
    vertical2 = dist(p3, p5)
    horizontal = dist(p1, p4)

    ear = (vertical1 + vertical2) / (2.0 * horizontal)
    return ear

# Calculate Mouth Aspect Ratio (MAR)
def calc_MAR(landmarks):
    top_lip = landmarks[13]
    bottom_lip = landmarks[14]
    left_lip = landmarks[78]
    right_lip = landmarks[308]

    mar = dist(top_lip, bottom_lip) / dist(left_lip, right_lip)
    return mar

# ----------------------------- #
# Main Code
# ----------------------------- #

# ----------------------------- # # MediaPipe FaceMesh Setup # ----------------------------- #
mp_face = mp.solutions.face_mesh.FaceMesh(
    static_image_mode=False,       
    max_num_faces=1,              
    refine_landmarks=True,         
    min_detection_confidence=0.5,  
    min_tracking_confidence=0.5    
)


EYE_LEFT = [33, 160, 158, 133, 153, 144]
EYE_RIGHT = [263, 387, 385, 362, 380, 373]

# Thresholds
EAR_THRESHOLD = 0.20
MAR_THRESHOLD = 0.60
FRAME_LIMIT = 15

closed_frames = 0

print("Opening webcam...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Could not access webcam.")
    raise SystemExit

print("Webcam successfully opened!")



while True:
    ok, frame = cap.read()
    if not ok:
        print("ERROR: Could not read frame.")
        break

    

    # Display exit instruction
    cv2.putText(frame, "Press C to exit", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    
    # Convert to RGB for MediaPipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_face.process(rgb)
    
    # If a face is detected
    if results.multi_face_landmarks:
        face = results.multi_face_landmarks[0]
        landmarks = face.landmark
        
        # EAR calculation
        ear_left = calc_EAR(landmarks, EYE_LEFT)
        ear_right = calc_EAR(landmarks, EYE_RIGHT)
        ear = (ear_left + ear_right) / 2.0

        # MAR calculation
        mar = calc_MAR(landmarks)

       
        # ----------------------------- # # Drowsiness Detection # ----------------------------- #
        # Sleep detection
        if ear < EAR_THRESHOLD:
            closed_frames += 1
            if closed_frames >= FRAME_LIMIT:
                cv2.putText(frame, "WARNING: DROWSINESS DETECTED!", (20, 140),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255), 3)
                winsound.Beep(1000, 500)
                cv2.imwrite("drowsiness_detected.png", frame)
        else:
            closed_frames = 0

       # ----------------------------- # # Yawn Detection # ----------------------------- #
        if mar > MAR_THRESHOLD:
            cv2.putText(frame, "WARNING: YAWN DETECTED!", (20, 200),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255), 3)
            cv2.imwrite("yawn_detected.png", frame)

    else:
        cv2.putText(frame, "Face not detected", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cap.release()
cv2.destroyAllWindows()
