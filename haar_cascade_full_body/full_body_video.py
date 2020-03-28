import cv2
import numpy as np

camera = cv2.VideoCapture('video.mp4')
full_body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while(1):
    ret , frame = camera.read()
    griton = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    bodies = full_body_cascade.detectMultiScale(griton , 1.1 , 4)

    for(x,y,w,h) in bodies:
        cv2.rectangle(frame , (x,y) , (x+w,x+h) , (0,255,0) , 3)

    cv2.imshow('insanlar', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()