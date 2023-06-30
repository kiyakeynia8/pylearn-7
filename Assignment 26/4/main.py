import cv2
import numpy as np
  
image = np.zeros((500, 500), np.uint8)

image[50:380,100:125] = 255

for i in range(12):
    i *= 10
    image[165-i:200-i,125+(i*2):145+(i*2)] = 255

for i in range(12):
    i *= 10
    image[200+i:235+i,125+(i*2):145+(i*2)] = 255

cv2.imshow("image", image)
cv2.waitKey()
cv2.imwrite("4/output.png",image)