import cv2
import numpy as np

image_sajjad = cv2.imread("input/sajjad.jpg")
image_lion = cv2.imread("input/lion.jpg")

image_sajjad = cv2.cvtColor(image_sajjad, cv2.COLOR_BGR2GRAY)
image_lion = cv2.cvtColor(image_lion, cv2.COLOR_BGR2GRAY)

image_sajjad = image_sajjad.astype(np.float32)
image_lion = image_lion.astype("float32")

# result = image_human + image_horse
# result = cv2.add(image_sajjad,image_lion)
result = (image_lion*1/4 + image_sajjad*2/4)

result = result.astype(np.uint8)

cv2.imshow("output",result)
cv2.waitKey()
cv2.imwrite("output/result4.jpg", result)