import cv2
import numpy as np

resim = cv2.imread('kose-bulma.jpg')
griton = cv2.cvtColor(resim , cv2.COLOR_BGR2GRAY)
griton = np.float32(griton)

koseler = cv2.goodFeaturesToTrack(griton , 300 , 0.01 , 10) #max nokta sayısı , hassasiyet , mesafe
koseler = np.int0(koseler) #floatken koseleri tespit ettik en baştaki haline döndürdük

for kose in koseler:
    x,y = kose.ravel() #x y koordinatlarını aldık
    cv2.circle(resim , (x,y) , 3 , 255 , -1) #3 yarıcap 255 renk

cv2.imshow('koseler' , resim)
cv2.waitKey(0)
cv2.destroyAllWindows()