import numpy as np 
import cv2

cap = cv2.VideoCapture("ronaldinho.mp4")
delay =33
idx = 0 

w = 640
h = 480

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = 'output.mp4'
fps = 30
out = cv2.VideoWriter(output_file,fourcc,fps,(w,h))

while(cap.isOpened()):
    ret, frame = cap.read()
    h,w,c = frame.shape
    
    if ret is False:
        # cap.release()
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        # cap = cv2.VideoCapture("ronaldinho.mp4")
        # cap.isOpened()
        #ret, frame = cap.read()
        continue 
        
    
    resized = cv2.resize(frame,(int(w/2),int(h/2)))
    #resized = cv2.resize(frame, (0,0),fx=0.5, fy = 0.5)
    cv2.imshow("resized",resized)
  
    
    key = cv2.waitKey(fps)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xff == ord('c'):
        cv2.imwrite("{0:03}.jpg".format(idx),frame)
        idx +=1

cap.release()
out.release()
cv2.destroyAllWindows()