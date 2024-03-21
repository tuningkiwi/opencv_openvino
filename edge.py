import cv2


src = cv2.imread("strawberry.webp", cv2.IMREAD_COLOR)
print(src.shape)

gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U)
canny = cv2.Canny(gray,100,150)



cv2.imshow("sobel",sobel)
cv2.imshow("laplacian",laplacian)
cv2.imshow("canny",canny)


cv2.waitKey()
cv2.destroyAllWindows()