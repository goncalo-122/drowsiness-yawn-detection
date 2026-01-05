Drowsiness and Yawn Detection (MediaPipe)
This project detects drowsiness (eyes closing) and yawning (mouth opening) in real time using a webcam and MediaPipe.
It uses two ratios:
•	EAR – Eye Aspect Ratio (detects eye closure)
•	MAR – Mouth Aspect Ratio (detects yawning)
Both are calculated from MediaPipe facial landmarks.
________________________________________
Features
•	Real time face and landmark detection
•	EAR and MAR calculation
•	Alerts for: 
o	Eyes closed (drowsiness)
o	Mouth open (yawn)
•	drowsiness and  yawn Screenshot
•	Lightweight and fast
________________________________________
Tech Stack
•	Python 3.12
•	MediaPipe 0.10.18
•	OpenCV 4.12.0
•	NumPy 1.26.4
•	Windows
________________________________________
Installation
python -m venv .venv
.\.venv\Scripts\activate
pip install --upgrade pip
pip install opencv-python mediapipe==0.10.18 numpy
________________________________________
Run
python main.py
________________________________________
Controls
•	Press c to exit
________________________________________
How It Works
•	MediaPipe detects 478 facial landmarks
•	EAR measures eye openness
•	MAR measures mouth opening
•	Thresholds decide: 
o	Drowsiness → EAR low for several frames
o	Yawn → MAR high
________________________________________
Author
Gonçalo Nova 
Version 1.0
________________________________________
