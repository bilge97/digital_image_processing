import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while(1):
    ret , frame = camera.read()

    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV) #formatı hsv ye çevirdik HSV de renk, doygunluk ve parlaklık değerleri kullanılır
    dusukKirmizi = np.array([150,30,30])
    ustKirmizi = np.array([190,255,255])#kırmızı filtreledik

    mask = cv2.inRange(hsv , dusukKirmizi , ustKirmizi)
    sonResim = cv2.bitwise_and(frame , frame , mask= mask)

    dusukMavi = np.array([100, 60, 60])
    ustMavi = np.array([140, 255, 255])

    dusukBeyaz = np.array([0,0,140])
    ustBeyaz = np.array([256,60,256])

    cv2.imshow('original' , frame)
    cv2.imshow('mask' , mask)
    cv2.imshow('sonResim' , sonResim)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()