import numpy as np
import cv2


#이미지 파일을 read
img = cv2.imread("dune.jpg")

#image란 이름의 display 창 생성 
cv2.namedWindow("image",cv2.WINDOW_NORMAL)

#numpy ndarray H/W/C/ Order
print(img.shape)

#read한 이미지 파일을 display 
cv2.imshow("image",img)

cv2.waitKey(0)

cv2.imwrite("output.jpg".img)

cv2.destroyAllWindows()