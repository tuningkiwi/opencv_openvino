import cv2
import numpy as np

src = cv2.imread("strawberry.webp", cv2.IMREAD_COLOR)
print(src.shape)

b = src[:,:,0]
g = src[:,:,1]
r = src[:,:,2]

inverse = cv2.merge((r,g,b))

h, w, c = src.shape
zero = np.zeros((h,w,1),dtype=np.uint8)
dst = cv2.merge((b,g,zero))

cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
cv2.imshow("inverse", inverse)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()