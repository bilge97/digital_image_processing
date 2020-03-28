import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while(1):
    ret , frame = camera.read()

    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV) #formatı hsv ye çevirdik HSV de renk, doygunluk ve parlaklık değerleri kullanılır
    dusukMavi = np.array([100, 60, 60])
    ustMavi = np.array([140, 255, 255])

    #laplacian = cv2.Laplacian(frame , cv2.CV_64F)
    #sobelX = cv2.Sobel(frame , cv2.CV_64F,1,0 , ksize=5) #ksize ne kadarlık pixel aralıklarıyla kenar tespiti yapsın
    #sobelY = cv2.Sobel(frame , cv2.CV_64F,0,1 , ksize=5)

    kenarlar = cv2.Canny(frame , 100 , 200) #eşik değerleriyle oyna


    mask = cv2.inRange(hsv , dusukMavi , ustMavi)
    sonResim = cv2.bitwise_and(frame , frame , mask= mask)


    cv2.imshow('original' , frame)
    #cv2.imshow('laplacian' , laplacian)
    #cv2.imshow('sobelX' , sobelX)
    #cv2.imshow('sobelY' , sobelY)
    cv2.imshow('kenarlar' , kenarlar)




    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()