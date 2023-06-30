import cv2
import numpy as np

image = ...

cv2.rectangle(image,(30,35), (350,410), 128, 4)

cv2.imshow("output", image)
cv2.waitKey()