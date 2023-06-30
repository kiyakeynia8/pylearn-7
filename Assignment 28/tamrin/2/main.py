import cv2

image = cv2.imread("tamrin/2/im1.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface_extended.xml")
faces = face_detector.detectMultiScale(image)

print(len(faces))

cv2.imshow("result", image)
cv2.waitKey()