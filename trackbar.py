import numpy as np 
import cv2 

cap = cv2.VideoCapture(0)

topLeft = (100,100)
bold = 0 
fps = 33
idx = 0 
fontsize=0

R,G,B = 0,0,0

def on_bold_trackbar(value):
    global bold
    bold = value
    pass

def on_fontsize_trackbar(value):
    global on_fontsize
    fontsize = value
    
def on_R_trackbar(value):
    global R
    R = value
    
def on_G_trackbar(value):
    global G
    G = value

def on_B_trackbar(value):
    global B
    B = value


cv2.namedWindow("camera")
cv2.createTrackbar("bold","camera",bold,10,on_bold_trackbar)
cv2.createTrackbar("Rcolor","camera",R,10,on_R_trackbar)
cv2.createTrackbar("Gcolor","camera",G,10, on_G_trackbar)
cv2.createTrackbar("Bcolor","camera",B,10, on_B_trackbar)
cv2.createTrackbar("fontsize","camera",fontsize,10, on_fontsize_trackbar)



while(cap.isOpened()):
    
    ret,frame = cap.read()
    if ret is False: 
        print("can't recieve frame")
        break
    
    cv2.putText(frame, "Hello World",topLeft,cv2.FONT_HERSHEY_SIMPLEX,fontsize+1,(B,G,R),1+bold)
    
    cv2.imshow("camera",frame)
    key = cv2.waitKey(fps)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xff == ord('c'):
        cv2.imwrite("{0:03}.jpg".format(idx),frame)
        idx +=1

cap.release()
cv2.destroyAllWindows()

