import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

_, frame = cap.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
rows ,cols  = frame.shape
writer = cv2.VideoWriter("4/output_4.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

while True:
    ret, frame = cap.read()
    
    frame[220:260,300:305] = 0
    frame[220:225,300:340] = 0
    frame[260:265,300:340] = 0
    frame[220:265,340:345] = 0

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    check = frame[225:260,305:340]

    if 0 < np.average(check) < 80:
        cv2.putText(frame,"Black",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)
    
    elif 120 < np.average(check) < 225:
        cv2.putText(frame,"white",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)
    
    else:
        cv2.putText(frame,"gray",(280,300),cv2.FONT_ITALIC,1,(0,0,0),2)

    if not ret:
        break

    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()