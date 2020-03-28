import cv2
import numpy as np

img_rgb = cv2.imread('eller.jpg')
img_gray = cv2.cvtColor(img_rgb , cv2.COLOR_BGR2GRAY)

nesne = cv2.imread('el.png' , 0)

width , height = nesne.shape[::-1]

res = cv2.matchTemplate(img_gray , nesne , cv2.TM_CCOEFF_NORMED)
threshold = 0.8

loc = np.where(res>threshold)

for n in zip(*loc[::-1]):
    cv2.rectangle(img_rgb , n , (n[0]+width , n[1]+height) , (0,255,255) , 1)
cv2.imshow('bulunan el' , img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()