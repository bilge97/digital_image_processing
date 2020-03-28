import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('sudoku.JPG' , 0)
image=cv2.medianBlur(image , 5)

ret , th1 = cv2.threshold(image , 127 , 255 , cv2.THRESH_BINARY) # 127den yüksek değerleri beyaz , kücükleri 0 algılar
th2 = cv2.adaptiveThreshold(image , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 11 , 2) # max value 255 komşuların ortalamasını alarak thresh yapar , kaç pixel komşunun ort değerini alsın 11
th3 = cv2.adaptiveThreshold(image , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 11 , 2) # komşuların ağırlıklı ortalamasını alarak thresh yapar gerçekçi

basliklar = ['Original' , 'Basit Thresholding(127)' , 'MEAN_C' , 'GAUSSIAN_C']
resimler = [image , th1 , th2 , th3]

for i in range(4):
    plt.subplot(2 , 2 , i+1) , plt.imshow(resimler[i] , 'gray')
    plt.title(basliklar[i])
    plt.xticks([]), plt.yticks([])
plt.show()
