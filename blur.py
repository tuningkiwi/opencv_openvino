import cv2

src = cv2.imread("strawberry.webp", cv2.IMREAD_COLOR)
print(src.shape)

dst = cv2.blur(src, (9,9), anchor=(-1,-1), borderType=cv2.BORDER_TRANSPARENT)

cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()