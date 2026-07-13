import cv2
import serial
import time
import pyttsx3
import threading

# ==============================
# SERIAL SETUP
# ==============================
arduino = serial.Serial('COM9', 9600, timeout=2)
time.sleep(2)

# ==============================
# TEXT TO SPEECH SETUP
# ==============================
engine = pyttsx3.init()
engine.setProperty('rate', 200)

def speak_alert():
    """Function to speak Sleep Alert repeatedly in a separate thread."""
    global speaking
    while speaking:
        engine.say("Sleep Alert")
        engine.runAndWait()
        time.sleep(1)  # repeat every 1 sec

# ==============================
# LOAD HAAR CASCADES
# ==============================
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml"
)

# ==============================
# CAMERA SETUP
# ==============================
cap = cv2.VideoCapture(0)

ALARM_DELAY = 2  # seconds
eye_closed_start = None
alarm_active = False
speaking = False  # Flag for TTS thread

print("System Started...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eyes_detected = False
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        if len(eyes) > 0:
            eyes_detected = True

        # Draw rectangles
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    current_time = time.time()

    # ==============================
    # DROWSINESS LOGIC
    # ==============================
    if len(faces) > 0:
        if eyes_detected:
            status_text = "EYE OPEN"
            color = (0, 255, 0)
            eye_closed_start = None

            # Stop TTS if previously speaking
            if speaking:
                speaking = False
                time.sleep(0.1)  # give thread time to stop
        else:
            if eye_closed_start is None:
                eye_closed_start = current_time

            elapsed_time = current_time - eye_closed_start

            if elapsed_time >= ALARM_DELAY:
                status_text = "SLEEP ALERT!"
                color = (0, 0, 255)
                arduino.write(b'0')  # Buzzer ON, Motor OFF
                alarm_active = True

                # Start TTS in separate thread if not already
                if not speaking:
                    speaking = True
                    threading.Thread(target=speak_alert, daemon=True).start()
            else:
                status_text = "BLINKING..."
                color = (0, 255, 255)
    else:
        status_text = "NO FACE"
        color = (255, 255, 255)

    # Display status
    cv2.putText(frame, status_text, (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Drowsiness Detection System", frame)

    key = cv2.waitKey(1) & 0xFF

    # 🔹 Press T to restart motor
    if key == ord('t') and alarm_active:
        arduino.write(b'1')  # Motor ON, Buzzer OFF
        alarm_active = False
        if speaking:
            speaking = False  # Stop TTS
            time.sleep(0.1)
        print("Motor Restarted")

    # ESC to exit
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()