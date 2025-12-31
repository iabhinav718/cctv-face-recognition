import cv2
import numpy as np
import face_recognition
import os

path = 'known_faces'
images = []
classNames = []

for file in os.listdir(path):
    img = cv2.imread(os.path.join(path, file))
    if img is not None:
        images.append(img)
        classNames.append(os.path.splitext(file)[0])

print(f"Loaded {len(images)} known faces:", classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(rgb_img)
        if len(encodes) > 0:
            encodeList.append(encodes[0])
    return encodeList

encodeListKnown = findEncodings(images)
print("Encoding complete!")

if not os.path.exists('unidentified'):
    os.makedirs('unidentified')

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        print("Camera not detected.")
        break

    imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        if len(faceDis) > 0:
            matchIndex = np.argmin(faceDis)
            if faceDis[matchIndex] < 0.45:
                name = classNames[matchIndex].upper()
            else:
                name = "UNIDENTIFIED"
        else:
            name = "UNIDENTIFIED"

        y1, x2, y2, x1 = [v * 4 for v in faceLoc]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name, (x1 + 6, y2 - 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        if name == "UNIDENTIFIED":
            face_crop = frame[y1:y2, x1:x2]
            if face_crop.size != 0:
                filename = f"unidentified/face_{np.random.randint(10000)}.jpg"
                cv2.imwrite(filename, face_crop)

    cv2.imshow('CCTV Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
