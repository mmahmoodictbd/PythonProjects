import cv2
import numpy as np
import time

# multiple cascades: https://github.com/opencv/opencv/tree/master/data/haarcascades

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if face_cascade.empty(): raise Exception("your face_cascade is empty. are you sure, the path is correct ?")

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
if eye_cascade.empty(): raise Exception("your eye_cascade is empty. are you sure, the path is correct ?")

nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
if nose_cascade.empty(): raise Exception("your nose_cascade is empty. are you sure, the path is correct ?")

video_capture = cv2.VideoCapture(0)

# Find OpenCV version
# With webcam get(CV_CAP_PROP_FPS) does not work.
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
if int(major_ver)  < 3 :
    fps = video_capture.get(cv2.cv.CV_CAP_PROP_FPS)
    print "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)
else :
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    print "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps)
  

if video_capture.isOpened(): # try to get the first frame
    success, frame = video_capture.read()
else:
    success = False

while success:
    ret, frame = video_capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    height, width = gray_frame.shape
    min_size = (int(height/4), int(width/4)) 
    faces = face_cascade.detectMultiScale(gray_frame, 
                                          scaleFactor=1.1, 
                                          minNeighbors=2, 
                                          flags=cv2.CASCADE_SCALE_IMAGE, 
                                          minSize=min_size)

    # Draw a rectangle around the faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray_frame[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Detect eyes and draw a rectangle around the eyes
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        # Detect nose within the region bounded by each face
        nose = nose_cascade.detectMultiScale(roi_color)
        for (ex,ey,ew,eh) in nose:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('Webcam (Press q to close)', frame)

    keypress = cv2.waitKey(1)
    if keypress & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()