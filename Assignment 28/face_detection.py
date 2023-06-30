import cv2

image = cv2.imread("im3.jpg")
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2BGRA)
image_kia = cv2.imread("im1.jpg")
# image_kia_gray = cv2.cvtColor(image_kia,cv2.COLOR_BGR2BGRA)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
faces = face_detector.detectMultiScale(image_gray)

for face in faces:
    x,y,w,h = face
    # cv2.rectangle(image,[x,y],[x+w,y+h],[0,0,0],8)
    kia = cv2.resize(image_kia,[w,h])
    image[y:y+h, x:x+w] = kia

cv2.imshow("result", image)
cv2.waitKey()