import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(2)

if cap.isOpened(): # try to get the first frame
    success, frame = cap.read()
else:
    success = False

while success:

    cv2.imshow('WebCam (Press q to close)', frame)
    ret, frame = cap.read()

    # Gray frame
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray WebCam (Press q to close)', grayFrame)

    keypress = cv2.waitKey(1)
    if keypress & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()