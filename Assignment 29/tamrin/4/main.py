import cv2
import numpy as np

image_1 = cv2.imread("tamrin/4/im1.png",0)
image_2 = cv2.imread("tamrin/4/im2.png",0)

image_1 = image_1.astype(np.float32)
image_2 = image_2.astype("float32")

result = image_2 - image_1

result = result.astype(np.uint8)

cv2.imshow("output",result)
cv2.waitKey()
cv2.imwrite("tamrin/4/output_4.jpg", result)