import numpy as np 
import cv2 

cap = cv2.VideoCapture(0)

w= 640
h =480

cap.set(cv2.CAP_PROP_FRAME_WIDTH,w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)


while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret is False: 
        print("can't receive frame")
        break
    
    cv2.imshow("camera",frame)
    
    key = cv2.waitKey(33)
    if key & 0xFF == ord('q'):
        break

