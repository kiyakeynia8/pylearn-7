import cv2

def chess_face(image):
    frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray,1.3)
    for face in faces:
        x,y,w,h = face
        face_image = image[y:y+h,x:x+w]
        face_image_spall = cv2.resize(face_image,[10,10])
        face_image_big = cv2.resize(face_image_spall,[w,h],interpolation=0)
        image[y:y+h,x:x+w] = face_image_big
    return image


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

while True:
    _, frame = cap.read()

    image = chess_face(frame)

    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break