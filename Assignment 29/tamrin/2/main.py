import cv2
import numpy as np

images = [[None for i in range(5)] for j in range(4)]
result_image = []
result = np.zeros((2000, 2000), dtype= np.uint8)
for i in range(4):
    result_image.append(0)

def read_and_run():
    for i in range(4):
        for j in range(5):
            images[i][j] = cv2.imread(f"tamrin/2/inputs/{i+1}/{j+1}.jpg",0)
            images[i][j] = images[i][j].astype(np.float32)

    for i in range(4):
        for j in range(5):
            result_image[i] += (images[i][j] / 10)
        result_image[i] = result_image[i].astype(np.uint8)

read_and_run()

result[0:1000, 0:1000] = result_image[0]
result[0:1000, 1000:2000] = result_image[1]
result[1000:2000, 0:1000] = result_image[2]
result[1000:2000, 1000:2000] = result_image[3]

cv2.imshow("result",result)
cv2.waitKey()
cv2.imwrite("tamrin/2/output_2.jpg",result)