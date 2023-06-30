import cv2

image_1 = cv2.imread("input/a.tif")
image_2 = cv2.imread("input/b.tif")

# result = image_1 - image_2
result = cv2.subtract(image_1,image_2)

result = result -255

cv2.imshow("output",result)
cv2.waitKey()
cv2.imwrite("output/result6.jpg", result)