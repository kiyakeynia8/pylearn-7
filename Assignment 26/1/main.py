import cv2

my_board = cv2.imread("1/gray.jpg")

shape_board = my_board.shape
print(shape_board)

b_or_w = 0

for i in range(int((shape_board[0])/25)):
    for j in range(int((shape_board[1])/25)):
        my_board[j*28: (j+1)*28,i* 28: (i+1)*28] = b_or_w

        if b_or_w == 255:
            b_or_w = 0
        else:
            b_or_w = 255

cv2.imshow("my image", my_board)
cv2.waitKey()
cv2.imwrite("1/output.png",my_board)