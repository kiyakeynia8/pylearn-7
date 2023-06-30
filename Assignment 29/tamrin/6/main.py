import cv2 

main_image = cv2.imread("tamrin/6/im2.jpg")
u = cv2.imread("tamrin/6/im1.jpg")
d = cv2.imread("tamrin/6/im3.jpg")
shape = main_image.shape

for i in range(shape[0]):
    for j in range(shape[1]):
        a = main_image[i,j]
        if a[0] == 0 and a[1] == 0:
            main_image[i,j] = u[i,j]
        else:
            main_image[i,j] = d[i,j]
        
cv2.imshow("result",main_image)
cv2.waitKey()
cv2.imwrite("tamrin/6/output_6.jpg",main_image)