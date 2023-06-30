import cv2
import random

image = cv2.imread("3/im1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image,(700,500))
b_y, b_x = image.shape
snows = []

number = random.randint(1000,2000)

for i in range(number):
    y = random.randint(-500, b_y)
    x = random.randint(0, b_x)
    rand_x = random.randint(-1, 1)
    snows.append([y, x, rand_x])
    image[snows[i][0]: snows[i][0] + 2, snows[i][1]: snows[i][1] + 2] = 255
    snows[i][0] += 5
    snows[i][1] += rand_x

rows = image.shape[0]
cols = image.shape[1]
writer = cv2.VideoWriter("3/output_3.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))


while True:
    image = cv2.imread("3/im1.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image,(700,500))
    for i in range(number):
        rand_x = snows[i][2]
        image[snows[i][0]: snows[i][0] + 2, snows[i][1]: snows[i][1] + 2] = 255
        snows[i][0] += 5
        snows[i][1] += rand_x
    
    image = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
    writer.write(image)
    cv2.imshow("result",image)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()