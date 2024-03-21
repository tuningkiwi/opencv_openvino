import numpy as np 
import cv2 

cap = cv2.VideoCapture(0)

topLeft = (50,50)
bottomRight = (300,300)
fps = 30
idx = 0

point = (200,200)
radius = 50 
def click(event, x,y, flags, param):
    global point
    if event ==cv2.EVENT_LBUTTONDOWN:
        print("Pressed",x,y)
        point = (x,y)


cv2.namedWindow("camera")
cv2.setMouseCallback("camera",click)


while(cap.isOpened()):
    
    ret,frame = cap.read()
    
    cv2.line(frame,topLeft, bottomRight, (0,255,0),5)
    
    cv2.rectangle(frame, [pt+30 for pt in topLeft],[pt-30 for pt in bottomRight],(0,0,255),5)
    cv2.circle(frame, point, radius, (200,100,0),3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'me',[pt+80 for pt in topLeft], font, 2, (0,255,255),10)
    
    cv2.imshow("camera",frame)
    
    key = cv2.waitKey(fps)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xff == ord('c'):
        cv2.imwrite("{0:03}.jpg".format(idx),frame)
        idx +=1

cap.release()
cv2.destroyAllWindows()

