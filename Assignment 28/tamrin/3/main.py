import cv2
import cvzone

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
key = None
_, frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]

writer = cv2.VideoWriter("outputs_assignment28/output_3.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if key == 1:
        wolf_img = cv2.imread("tamrin/3/im2.png", cv2.IMREAD_UNCHANGED)
        faces = face_detector.detectMultiScale(frame, 1.3)
        for face in faces:
            x,y,w,h = face
            image = cv2.resize(wolf_img, [w, h])
            frame = cvzone.overlayPNG(frame, image, [x, y])

    elif key == 2:
        wolf_img = cv2.imread("tamrin/3/im1.png", cv2.IMREAD_UNCHANGED)
        faces = face_detector.detectMultiScale(frame, 1.3)
        for face in faces:
            x,y,w,h = face
            image = cv2.resize(wolf_img, [w, h])
            frame = cvzone.overlayPNG(frame, image, [x, y])

    elif key == 3:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(frame_gray,1.3)
        for face in faces:
            x,y,w,h = face
            face_image = frame[y:y+h,x:x+w]
            face_image_spall = cv2.resize(face_image,[10,10])
            face_image_big = cv2.resize(face_image_spall,[w,h],interpolation=0)
            frame[y:y+h,x:x+w] = face_image_big

    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow('result',frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(5) & 0xFF == ord('1'):
        key = 1
    elif cv2.waitKey(5) & 0xFF == ord('2'):
        key = 2
    elif cv2.waitKey(5) & 0xFF == ord('3'):
        key = 3

writer.release()