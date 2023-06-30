import cv2

# image = cv2.imread("2/im1.png")
image = cv2.imread("2/im2.png")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

rows , cols = image.shape

for r in range(rows):
    for c in range(cols):
        image[r,c] = 255 - image[r,c]

cv2.imshow("output",image)
cv2.waitKey()
# cv2.imwrite("2/output.png",image)
cv2.imwrite("2/output2.png",image)