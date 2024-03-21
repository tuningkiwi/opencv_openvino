import numpy as np
import cv2


#이미지 파일을 read
color = cv2.imread("strawberry.webp", cv2.IMREAD_COLOR)
print(color.shape)

height,width,channels = color.shape
cv2.imshow("original image",color)

b,g,r = cv2.split(color)
rgb_split = np.concatenate((b,g,r),axis =1)
cv2.imshow("BGR Channels", rgb_split)

hsv = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)

#read한 이미지 파일을 display 
cv2.imshow("image",hsv_split)

rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
cv2.imshow("rgb image",rgb)


cv2.waitKey(0)

cv2.destroyAllWindows()