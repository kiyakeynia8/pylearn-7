import cv2

cap = cv2.VideoCapture(0)

_, frame = cap.read()

while True:
    _, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break