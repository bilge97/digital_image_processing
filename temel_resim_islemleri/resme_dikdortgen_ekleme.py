import cv2

img = cv2.imread('cicek.png')
cv2.imshow('Cicek' , img)

cv2.rectangle(img , (200,70) , (320,180) , (255 ,0,0) , 2 ) #img,dörtgen başlangıç , bitim , color ,line kalınlığı
cv2.imshow('Dortgen' , img)

cv2.waitKey(0)
cv2.destroyAllWindows()