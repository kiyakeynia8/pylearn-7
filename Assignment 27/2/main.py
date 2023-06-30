import cv2
import numpy as np

tv_image = cv2.imread("2/im1.png")
rows = tv_image.shape[0]
cols = tv_image.shape[1]

shape = tv_image.shape

for i in range(rows):
    for j in range(cols):
        print(tv_image[i,j])

# writer = cv2.VideoWriter("2/output_2.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

# while True:
#     tv_image = cv2.imread("2/im1.png")
#     tv_image = cv2.cvtColor(tv_image,cv2.COLOR_BGR2GRAY)
#     noise = np.random.random((115 ,150)) * 255
#     noise = np.array(noise,dtype=np.uint8)

#     tv_image[22:137, 26:176] = noise

#     tv_image = cv2.cvtColor(tv_image,cv2.COLOR_GRAY2BGR)
#     writer.write(tv_image)
#     cv2.imshow("result", tv_image)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# writer.release()