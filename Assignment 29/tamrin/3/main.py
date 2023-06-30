import cv2

image = cv2.imread("tamrin/3/im1.jpg",0)

result = (image / (255 - cv2.GaussianBlur(255 - image,(21,21), 0))) * 255

cv2.imwrite("tamrin/3/output_3.jpg", result)