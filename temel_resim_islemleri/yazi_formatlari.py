import cv2
import numpy as np

def metin_yaz():
    img = np.zeros((640,720,3) , np.uint8) #ne kadar alan kullanacaksın,alan oluştur
    img.fill(255) #comple beya göründü

    fontscale = 1.0
    color = (0,0,255) #mavi yeşil kırmızı
    fontface = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img , "FONT_HERSHEY_COMPLEX" , (25,40) , fontface , fontscale,color)

    cv2.namedWindow('text ornekler')
    cv2.imshow('ornekler' , img)
    cv2.imwrite('text_ornek.jpg' , img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    metin_yaz()

if __name__ == '__main__':
    main()