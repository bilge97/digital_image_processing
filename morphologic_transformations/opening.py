import cv2
import numpy as np

camera = cv2.VideoCapture(0)
#hataları silme gürültüleri yani

while(1):
    ret , frame = camera.read()

    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV) #formatı hsv ye çevirdik HSV de renk, doygunluk ve parlaklık değerleri kullanılır

    dusukMavi = np.array([100, 60, 60])
    ustMavi = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, dusukMavi, ustMavi)
    sonResim = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5,5) , np.uint8)

    erosion = cv2.erode(mask , kernel,iterations=1) #gürültü siler
    dilation = cv2.dilate(mask , kernel , iterations=1) #gürültüyü belirginleştirir

    opening = cv2.morphologyEx(mask , cv2.MORPH_OPEN , kernel) #filtrenin içinde uymayan kısımları belirginleştirir
    closing = cv2.morphologyEx(mask , cv2.MORPH_CLOSE , kernel) #uymayan kısımları sanki filtrenin elemanıymış gibi beyaz yaptı

    cv2.imshow('original' , frame)
    cv2.imshow('mask' , mask)
    cv2.imshow('sonResim' , sonResim)
    cv2.imshow('erosion' , erosion)
    cv2.imshow('dilation' , dilation)
    cv2.imshow('opening' , opening)
    cv2.imshow('closing' , closing)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()