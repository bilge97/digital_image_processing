import cv2
import numpy as np

img = cv2.imread('kalabalik2.jpg')

yuz_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')

griton = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
yuzler = yuz_cascade.detectMultiScale(griton , 1.1 ,4)#yüzde 10 büüyültsün , min 4 defa arasın var mı diye teyit etsin.

for (sol_ust_x , sol_ust_y , weight , height) in yuzler:
    cv2.rectangle(img , (sol_ust_x , sol_ust_y), (sol_ust_x+weight , sol_ust_y+height) , (0,255,0) , 3)

cv2.imshow('yuzler' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()