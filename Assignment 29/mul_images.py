import cv2

image_1 = cv2.imread("input/c.tif")
image_mask = cv2.imread("input/d.tif")

image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
image_mask = cv2.cvtColor(image_mask, cv2.COLOR_BGR2GRAY)

image_mask = image_mask / 255.0

result = image_1 * image_mask

cv2.imshow("output",result)
cv2.waitKey()
cv2.imwrite("output/result7.jpg", result)