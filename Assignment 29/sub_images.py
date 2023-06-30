import cv2
import numpy as np

image_1 = cv2.imread("input/d1.bmp")
image_2 = cv2.imread("input/d2.bmp")

image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)

image_1 = image_1.astype(np.float32)
image_2 = image_2.astype("float32")

result = image_1 - image_2

result = result.astype(np.uint8)

cv2.imshow("output",result)
cv2.waitKey()
cv2.imwrite("output/result5.jpg", result)