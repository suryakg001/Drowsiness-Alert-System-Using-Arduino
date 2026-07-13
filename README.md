# 🚗 Drowsiness Alert System Using Arduino

A real-time **Driver Drowsiness Detection and Alert System** developed using **Python, OpenCV, and Arduino UNO**. This project monitors the driver's eyes through a webcam and detects prolonged eye closure. When drowsiness is detected, the system immediately activates a **buzzer**, **LED indicator**, and **16x2 LCD display** through Arduino to alert the driver and help prevent road accidents.

## 📌 Features

* 👁️ Real-time eye detection using OpenCV
* 😴 Detects driver drowsiness based on eye closure
* 🔊 Activates buzzer when drowsiness is detected
* 💡 Turns ON LED warning indicator
* 📺 Displays alert message on 16x2 LCD
* 🔄 Arduino and Python communicate via Serial Communication
* ⚡ Fast and lightweight implementation

## 🛠️ Technologies Used

* Python 3
* OpenCV
* Arduino UNO
* MediaPipe / Haar Cascade (depending on implementation)
* PySerial
* Pyttsx3 (Text-to-Speech)
* Embedded C (Arduino IDE)

## 🔧 Hardware Components

* Arduino UNO
* USB Webcam
* 16x2 LCD Display
* Active Buzzer
* LED
* Jumper Wires
* Breadboard
* USB Cable

## 📂 Project Structure

```
Drowsiness-Alert-System-Using-Arduino/
│
├── Arduino/
│   └── Arduino_Code.ino
│
├── Python/
│   └── drowsiness_detection.py
│
├── Images/
│
├── README.md
└── requirements.txt
```

## ⚙️ Working Principle

1. The webcam continuously captures the driver's face.
2. OpenCV detects the eyes in real time.
3. If the eyes remain closed for a predefined duration, the system identifies the driver as drowsy.
4. Python sends a signal to the Arduino through the serial port.
5. Arduino activates:

   * Buzzer
   * LED
   * LCD Warning Message
6. The alarm stops automatically once the driver's eyes reopen.

## 🚀 Installation

1. Clone the repository.
2. Install the required Python libraries:

```bash
pip install opencv-python pyserial pyttsx3 mediapipe
```

3. Upload the Arduino sketch using the Arduino IDE.
4. Update the correct COM port in the Python script.
5. Run the Python program.

## 🎯 Applications

* Driver Safety Systems
* Smart Vehicle Monitoring
* Road Accident Prevention
* College Mini Projects
* Embedded Systems Projects
* Computer Vision Projects

## 📈 Future Improvements

* GSM module for emergency SMS alerts
* GPS location tracking
* Cloud-based monitoring
* Mobile application support
* AI-based fatigue prediction
* Night vision camera support

## 🤝 Contribution

Contributions, suggestions, and improvements are welcome. Feel free to fork this repository and submit a pull request.

## 📄 License

This project is intended for educational and research purposes.

## 👨‍💻 Author

**Surya Prakash S**

If you found this project useful, please ⭐ Star this repository and share it with others.
