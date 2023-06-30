import cv2

my_image = cv2.imread("gray.jpg")
# my_image2 = cv2.cvtColor(my_image,cv2.COLOR_BGR2GRAY)

my_image[0:12, 0:225] = 0
my_image[0:225, 0:12] = 0
my_image[213:255, 0:225] = 0
my_image[0:225, 213:225] = 0

pepsi = my_image[103:143, 43:103]

my_image[140:180, 40:100] = pepsi

cv2.imshow("my image", my_image)
cv2.waitKey()
# cv2.imwrite("gray.jpg",my_image2)