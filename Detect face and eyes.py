import numpy as np
import cv2

# Load the cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Read the image
img = cv2.imread('vd.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Loop over each face detected
for (x, y, w, h) in faces:
    # Draw rectangle around the face
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Region of interest (ROI) for eyes within the face region
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    # Detect eyes within the face region
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # Loop over each eye detected and draw rectangle around each eye
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# Display the image with face and eye detection
cv2.imshow('img', img)

# Wait for a key press and close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
