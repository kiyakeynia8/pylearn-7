import cv2

image = cv2.imread("im3.jpg")
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2BGRA)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
faces = face_detector.detectMultiScale(image_gray)

for face in faces:
    x,y,w,h = face
    face_image = image[y:y+h,x:x+w]
    face_image_spall = cv2.resize(face_image,[20,20])
    face_image_big = cv2.resize(face_image_spall,[w,h],interpolation=0)
    image[y:y+h,x:x+w] = face_image_big

cv2.imshow("result", image)
cv2.waitKey()