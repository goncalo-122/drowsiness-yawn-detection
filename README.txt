Drowsiness and Yawn Detection using MediaPipe
This project uses Computer Vision to detect drowsiness (eye closure) and yawning (mouth opening) in real time using a webcam and MediaPipe Face Landmarker.

The system computes two biometric ratios:

EAR (Eye Aspect Ratio) for eye closure detection

MAR (Mouth Aspect Ratio) for yawn detection

Both are calculated from facial landmarks extracted by MediaPipe.

Features
Real-time face detection

EAR and MAR computation

Visual alerts for:

Drowsiness (eyes closed for multiple frames)

Yawning (mouth open beyond threshold)

Facial landmarks visualization (eyes and mouth)

Screenshot capture (optional)

Tech Stack and Versions
Python: 3.12

MediaPipe: 0.10.18

OpenCV: 4.12.0

NumPy: 1.26.4

OS: Windows

Requirements
Python 3.12

Webcam

MediaPipe 0.10.18

OpenCV 4.12.0

NumPy 1.26.4

Check Python version:
python --version

Installation
Create virtual environment:
python -m venv .venv

Activate virtual environment (PowerShell):
.\.venv\Scripts\activate

Install dependencies:
pip install --upgrade pip
pip install opencv-python mediapipe==0.10.18 numpy

Run the project
With the virtual environment active:
python main.py

Controls
Press c to exit the program

How it works (short explanation)
MediaPipe Face Landmarker detects 478 facial landmarks

EAR is computed from eye landmarks to measure eye openness

MAR is computed from mouth landmarks to measure mouth opening

Thresholds determine:

Drowsiness (EAR below threshold for several frames)

Yawn (MAR above threshold)

This approach is lightweight, fast, and suitable for real-time monitoring.

Author
Gonçalo Nova
Version: 1.0
Learning project focused on Computer Vision and real-time analysis.