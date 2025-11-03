# Real-Time Face Recognition System

A real-time facial recognition application built using **Python**, **OpenCV**, and **DeepFace**. The system detects and recognizes faces from a live webcam feed using deep learning-based facial embeddings — all processing is performed locally.

---

##  Overview

This project demonstrates a working prototype for real-time facial recognition on a local machine. It is intended for educational and controlled use only, with image data supplied by the user.

---

##  Features

- Real-time face detection
- Real-time face recognition
- Custom local face database
- Offline processing (no cloud dependencies)
- Virtual environment support

---

##  Requirements

- Python 3.10
- OpenCV
- DeepFace
- Mediapipe
- TensorFlow (compatible build)

---

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/face-recognition.git
cd face-recognition
```

Create and activate a virtual environment:

```bash
python -m venv venv
# For Windows
venv\Scripts\activate
# For Mac / Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

##  Project Structure

```
face_recognition/
│
├── faces/                 # User-provided training images (not included)
│   └── README.md          # Instructions for adding images
│
├── live_recognition.py    # Main real-time recognition script
├── face_detect.py         # Face detection test script
├── requirements.txt
└── README.md
```

---

##  Usage

1. **Test webcam and face detection**  
   ```bash
   python face_detect.py
   ```

2. **Run real-time face recognition**  
   ```bash
   python live_recognition.py
   ```

> Place clear, frontal images of known individuals in the `faces/` directory. One face per image is recommended.

---

##  Notes

- Use multiple clear images per person for improved accuracy.
- Press **Q** to exit the webcam window.
- Performance may vary with camera quality and lighting conditions.

---

##  Ethical Use

This project is intended for:
- Personal learning
- Research and experimentation
- Use with willing participants only

**Do not use for surveillance or without consent. All image data remains local.**

---

##  Potential Improvements

- Liveness / spoof detection
- GUI interface
- Face enrollment pipeline
- Logging or attendance system
- Edge deployment (e.g., Raspberry Pi)

---

