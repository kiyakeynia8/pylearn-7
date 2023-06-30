import cv2

image = cv2.imread("3/im1.png")
 
image = cv2.rotate(image, cv2.ROTATE_180)
 
cv2.imshow("rotate", image)
cv2.waitKey()
cv2.imwrite("3/output.png",image)