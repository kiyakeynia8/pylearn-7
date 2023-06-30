import cv2
import numpy as np
  
image = np.zeros((255, 255), np.uint8)
c,r = image.shape

for i in range(c):
    image[i:i+1,0:400] = i

cv2.imshow("image", image)
cv2.waitKey()
cv2.imwrite("5/output.png",image)