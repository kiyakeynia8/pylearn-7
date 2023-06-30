import cv2
import numpy as np

image_1 = cv2.imread('tamrin/1/im1.jpg')
image_2 = cv2.imread('tamrin/1/im2.jpg')
image_1 = cv2.resize(image_1,[500,500])
image_2 = cv2.resize(image_2,[500,500])

image_1 = image_1.astype(np.float32)
image_2 = image_2.astype(np.float32)

image_add_1 = (image_1*8/8 + image_2*0/8)
image_add_2 = (image_1*7/8 + image_2*1/8)
image_add_3 = (image_1*6/8 + image_2*2/8)
image_add_4 = (image_1*5/8 + image_2*3/8)
image_add_5 = (image_1*4/8 + image_2*4/8)
image_add_6 = (image_1*3/8 + image_2*5/8)
image_add_7 = (image_1*2/8 + image_2*6/8)

image_add_1 = image_add_1.astype(np.uint8)
image_add_2 = image_add_2.astype(np.uint8)
image_add_3 = image_add_3.astype(np.uint8)
image_add_4 = image_add_4.astype(np.uint8)
image_add_5 = image_add_5.astype(np.uint8)
image_add_6 = image_add_6.astype(np.uint8)
image_add_7 = image_add_7.astype(np.uint8)

image_add_1_7 = np.concatenate((image_add_1, image_add_2,image_add_3,image_add_4,image_add_5,image_add_6,image_add_7), 1)

cv2.imshow("result",image_add_1_7)
cv2.waitKey()
cv2.imwrite('tamrin/1/output_1.jpg',image_add_1_7)