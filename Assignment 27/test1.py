import cv2

image = cv2.imread("gray.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

rows , cols = image.shape

threshold = 100

# 1
# for r in range(rows):
#     for c in range(cols):
#         if image[r,c] > threshold:
#             image[r,c] = 255
#         else:
#             image[r,c] = 0

# 2
# image[image > threshold] = 255
# image[image < threshold] = 0

# 3
_,image = cv2.threshold(image,threshold,255,cv2.THRESH_BINARY)

cv2.imshow("",image)
cv2.waitKey()