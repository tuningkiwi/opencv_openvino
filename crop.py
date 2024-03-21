import numpy as np
import cv2


#이미지 파일을 read
img = cv2.imread("strawberry.webp")
print(img.shape)

cropped = img[50:450,100:400]
resized = cv2.resize(cropped,(400,200))

cv2.imshow("origin",img)
cv2.imshow("cropped img", cropped)
cv2.imshow("resized img", resized)


cv2.waitKey(0)

cv2.destroyAllWindows()