🦾 Animal Detection and Tranquilization System
Team DefTech | Smart India Hackathon 2024 (SIH1533)

Theme: Robotics and Drones | Category: Software + Hardware

📘 Overview

Human-wildlife conflict is a major issue in forest-adjacent and rural regions, where wild animals such as jackals often enter villages, causing damage and even loss of life. This project aims to prevent such encounters safely by detecting the presence of wild animals in real-time and automatically triggering an alert and tranquilization mechanism.

The system integrates AI-based image recognition, Arduino-controlled hardware, and automated tranquilization to protect both humans and animals.

🧩 System Features

🎯 Real-time Animal Detection using the MobileNetSSD deep learning model.

🔊 Automatic Alert System to warn nearby humans.

💉 Tranquilization Mechanism controlled by a piston motor to safely sedate the animal.

🔄 Hardware-Software Integration using Python and Arduino communication.

🌿 Non-lethal Solution ensuring animal safety and wildlife conservation.

⚙️ Tech Stack

Programming Languages: Python, C++ (Arduino)

Frameworks/Libraries: OpenCV, NumPy, PySerial

Model: MobileNetSSD (Caffe)

Hardware: Arduino UNO, Servo Motor/Piston, Camera Module, Buzzer, Sensors

🗂️ Project Files
File Name	Description
main.py	Main Python script for video capture, detection, and serial communication with Arduino.
MobileNetSSD_deploy.caffemodel	Pre-trained Caffe model for object detection.
MobileNetSSD_deploy.prototxt.txt	Model configuration file defining network layers and parameters.
testing.ino	Arduino code to control hardware actions (buzzer, servo/piston activation).
README.md	Project documentation and setup instructions.
🧠 How It Works

Camera Feed: Captures real-time video input.

Detection: The Python script uses MobileNetSSD to detect animals in the frame.

Signal Trigger: If an animal is detected, a signal is sent to the Arduino through a serial interface.

Hardware Action:

The buzzer/alarm alerts nearby humans.

The piston/servo motor fires a tranquilizer dart containing a mild, safe sleeping medicine.

Safety Protocol: The animal is sedated and can be relocated safely by authorities.

🪛 Installation & Setup
Software Setup

Clone the repository or download the project files.

Install dependencies:

pip install opencv-python numpy pyserial


Connect your camera and Arduino board via USB.

Load testing.ino onto the Arduino using the Arduino IDE.

Run the main program:

python main.py

Hardware Setup

Connect the buzzer to Arduino digital pin (e.g., D8).

Connect the servo motor/piston to pin (e.g., D9).

Ensure the tranquilizer mechanism is securely mounted.

Connect the camera module to the system (USB or PiCam).

🔍 Future Enhancements

Integration with thermal cameras for night detection.

Cloud-based data analytics and alerts via mobile app.

AI model training for specific regional animal species.

GPS-based tracking of sedated animals for monitoring.

🌍 Impact

🧑‍🌾 Social: Protects villagers and forest researchers from wild animal attacks.

🐾 Environmental: Uses a non-lethal method promoting animal safety.

💰 Economic: Reduces property damage and compensation expenses.

👥 Team DefTech

Innovating for safety and sustainability through intelligent robotics and automation.
