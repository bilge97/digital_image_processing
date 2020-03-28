import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sayfa.JPG')

img_medianblur = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(img , 30,255 , cv2.THRESH_BINARY) #125 altı beyaz 0lar

griton = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
ret, thgray = cv2.threshold(griton , 50,255 , cv2.THRESH_BINARY) #125 altı beyaz 0lar

gaus = cv2.adaptiveThreshold(griton , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 115 , 1)

ret , otsu = cv2.threshold(griton , 12 , 255 , cv2.THRESH_BINARY+cv2.THRESH_OTSU)

titles = ['original', 'threshbinart', 'thgray', 'gaus', 'otsu', 'median blur']
images = [img, th1, thgray, gaus, otsu, img_medianblur]

for i in range(6):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

#cv2.imshow('original' , img)
#cv2.imshow('threshbinary' , th1)
#cv2.imshow('thgray' , thgray)
#cv2.imshow('gaus' , gaus)
#cv2.imshow('otsu' , otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()