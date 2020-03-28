import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while(1):
    ret , frame = camera.read()

    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV) #formatı hsv ye çevirdik HSV de renk, doygunluk ve parlaklık değerleri kullanılır
    dusukMavi = np.array([100, 60, 60])
    ustMavi = np.array([140, 255, 255])

    mask = cv2.inRange(hsv , dusukMavi , ustMavi)
    sonResim = cv2.bitwise_and(frame , frame , mask= mask)

    #1.yontem
    kernel = np.ones((15,15) , np.float32) /225 #15 px e 15 px alan oluşturdum
    smoothed = cv2.filter2D(sonResim , -1 , kernel) #derinlik -1

    #2. yontem
    blur = cv2.GaussianBlur(sonResim , (15,15) , 0)

    #3.yontem
    median = cv2.medianBlur(sonResim , 15)
    bileteral = cv2.bilateralFilter(sonResim ,15 , 75 , 75)#bunu yapmazsam deli gibi bulanık oluyor

    cv2.imshow('original' , frame)
    cv2.imshow('sonResim' , sonResim)
    cv2.imshow('blur' , blur)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()