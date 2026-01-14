# CCTV Face Recognition System     
  
A real-time **CCTV face recognition system** built using **Python**, **OpenCV**, and the **face_recognition** library.
The system detects faces from a live camera feed, identifies known individuals, and automatically captures images of unidentified persons for further analysis.

---

## Project Objective

The main objective of this project is to design a **real-time surveillance-based face recognition system** that can:

* Identify known individuals using facial features
* Detect and label unknown individuals
* Store unidentified faces automatically for security review 
* Operate efficiently on live video streams    

This project demonstrates practical applications of **Computer Vision and Machine Learning** in surveillance systems.  

---

## Technologies Used

* **Python 3.11**
* **OpenCV (cv2)** – real-time image and video processing
* **face_recognition** – deep-learning-based face encoding and matching
* **NumPy** – numerical computations
* **Git & GitHub** – version control and project hosting

---

## Project Structure

```
cctv-face-recognition/
│
├── main.py                # Main program file
├── known_faces/           # Folder containing known face images
│   ├── abhinav.jpg
│   ├── plucky.jpg
│
├── unidentified/          # Automatically saved unknown faces
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
```

---

## How the System Works

1. Known face images are loaded from the `known_faces` directory.
2. Facial encodings are generated using deep learning.
3. The webcam captures live video frames.
4. Faces detected in real time are compared with known encodings.
5. If a match is found, the person’s name is displayed.
6. If no match is found, the face is labeled **UNIDENTIFIED** and saved locally.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/iabhinav718/cctv-face-recognition.git
cd cctv-face-recognition
```

### 2. Install Dependencies

Make sure Python **3.11** is installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Add Known Faces

* Place clear, front-facing images in the `known_faces` folder
* Name each image using the person’s name
  Example:

  ```
  abhinav.jpg
  ```

---

## Running the Project

```bash
python main.py
```

### Controls

* Press **Q** to exit the camera window

---

## Expected Output

* Webcam window opens
* Known faces are labeled with names
* Unknown faces are labeled **UNIDENTIFIED**
* Unknown faces are automatically saved in the `unidentified` folder

---

## Applications

* Smart CCTV surveillance systems
* Campus or office security
* Entry monitoring systems
* AI-based security research projects

---

## Limitations

* Accuracy depends on lighting and image quality
* Not optimized for large-scale databases
* Requires clear frontal face images

---

## Future Enhancements

* Add confidence scores for recognition
* Integrate database logging (CSV/SQL)
* Replace with advanced models (ArcFace, RetinaFace)
* Multi-camera support
* GPU acceleration

---

## Author





**Abhinav S**
BCA Student – Artificial Intelligence, Machine Learning & Robotics
Yenepoya University, Bangalore

