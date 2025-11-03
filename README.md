Real-Time Face Recognition System










A real-time facial recognition application built using Python, OpenCV and DeepFace.
The system detects and recognizes faces from a live webcam feed using deep learning-based facial embeddings.
All processing is performed locally.

Overview

This project demonstrates a working prototype for real-time facial recognition on a local machine.
It is intended for educational and controlled use only, with image data supplied by the user.

Features

Real-time face detection

Real-time face recognition

Custom local face database

Offline processing

Virtual environment support

Requirements

Python 3.10

OpenCV

DeepFace

Mediapipe

TensorFlow (compatible build)

Installation

Clone the repository:

git clone https://github.com/your-username/face-recognition.git
cd face-recognition


Create a virtual environment and activate:

python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # Mac / Linux


Install dependencies:

pip install -r requirements.txt

Project Structure
face_recognition/
│
├── faces/                 # User-provided training images (not included)
│   └── README.md          # Instructions for adding images
│
├── live_recognition.py    # Main real-time recognition script
├── face_detect.py         # Face detection test script
├── requirements.txt
└── README.md

Usage
1. Test camera and detection
python face_detect.py

2. Run face recognition
python live_recognition.py


Place images of known individuals in the faces/ directory
(one face per image recommended, clear frontal views).

Notes

Use multiple clear images per person for higher accuracy.

Press Q to exit webcam window.

System performance depends on camera quality and lighting conditions.

Ethical Use

This project is intended for:

Personal learning

Research / experimentation

Use with willing participants only

Do not deploy for surveillance or without consent.
All image data remains local.

Potential Improvements

Liveness / spoof detection

GUI interface

Face enrollment pipeline

Logging / attendance system

Edge deployment (Raspberry Pi)
