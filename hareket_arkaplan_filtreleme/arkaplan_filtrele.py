import numpy as np
import cv2

cap =cv2.VideoCapture('video.mp4')
foregroundbackground = cv2.createBackgroundSubtractorMOG2()

while True :
    ret , frame = cap.read()

    foreground_mask = foregroundbackground.apply(frame)

    cv2.imshow('foreground_mask' , foreground_mask)
    cv2.imshow('original' , frame)

    k = cv2.waitKey(25)
    if k == 27 :
        break
cap.release()
cv2.destroyAllWindows()