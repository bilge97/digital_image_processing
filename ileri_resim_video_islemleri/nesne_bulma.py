import cv2
import numpy as np


img_rgb = cv2.imread('ana-resim.jpg')
img_gray = cv2.cvtColor(img_rgb , cv2.COLOR_BGR2GRAY)

nesne = cv2.imread('template.jpg' , 0)

width , height = nesne.shape[::-1] #4 parametresi var 2 tanesini al w ve h yi

res = cv2.matchTemplate(img_gray , nesne , cv2.TM_CCOEFF_NORMED) #resmimizi eşleştirir
threshold = 0.8 #yüzde 80 doğrulu payıyla bulmayaçalış

loc  = np.where(res>threshold) #yüzde 80 büyük olunca tut

for n in zip(*loc[::-1]):
    cv2.rectangle(img_rgb , n , (n[0]+width,n[1]+height) , (0,255,255) , 2) #3. param dikdörtgenin başlangıç noktası n[0] sol üst x , 2 kalınlık


cv2.imshow('bulunan nesneler' , img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()


