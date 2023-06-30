import cv2
import numpy as np

while True:
    image = np.random.random((400,600)) * 255
    image = np.array(image,dtype=np.uint8)

    cv2.imshow("output", image)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break