import cv2

image = cv2.imread("6/im1.png")

for i in range(250):
    if i < 100:
        for j in range(100-i, 200-i):
            image[i, j] = 0
    else:
        for s in range(0, 200-i):
            image[i, s] = 0

cv2.imshow("output", image)
cv2.waitKey()
cv2.imwrite("6/output.png",image)