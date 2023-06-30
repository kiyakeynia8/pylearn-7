import cv2

image = cv2.imread("1/im1.PNG")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
c,r = image.shape

for i in range(c):
    for j in range(r):
        if 120 < image[i,j] > 130:
            image[i,j] = 0
        else:
            image[i,j] = 255

cv2.putText(image, 'BATMAN', (250, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, 255, 3)

cv2.imshow("output", image)
cv2.waitKey()
cv2.imwrite("1/output_1.PNG", image)