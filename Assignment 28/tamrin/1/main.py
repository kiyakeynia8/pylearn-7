import cv2
import numpy as np

my_bord = np.ones((550,900), dtype=np.uint8) * 255
rows , cols = my_bord.shape
w = 0

for i in range(int(cols/100)):
    if w == 0:
        my_bord[0:550,i*100:(i*100)+100] = 80
        w = 1
        
    else:
        my_bord[0:550,i*100:(i*100)+100] = 100
        w = 0

cv2.rectangle(my_bord,[10,10],[cols-10,rows-10],255,4)
cv2.rectangle(my_bord,[10,200],[50,350],255,4)
cv2.rectangle(my_bord,[10,150],[100,400],255,4)
cv2.rectangle(my_bord,[890,200],[850,350],255,4)
cv2.rectangle(my_bord,[890,150],[800,400],255,4)
cv2.circle(my_bord,[int(cols/2),int(rows/2)],5,255,10)
cv2.circle(my_bord,[int(cols/2),int(rows/2)],100,255,4)
cv2.line(my_bord, [int(cols/2),10],[int(cols/2),540],255,4)

cv2.imshow("result", my_bord)
cv2.waitKey()
cv2.imwrite("tamrin/1/output_1.PNG", my_bord)