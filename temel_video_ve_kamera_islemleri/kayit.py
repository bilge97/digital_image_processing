import cv2

camera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

#four character code : görüntü ve ses dosyaları çok büyük sıkıştırmak lazım.
#medya dosyalarında kullanılan codec’ler için pixel formatlarını, renk formatlarını, sıkıştırma formatlarını standart bir biçimde tanımlamlar.

kayit = cv2.VideoWriter('kayit.avi' , fourcc , 20.0 , (640,480)) #format , saniyede ne kadar görüntü alacağım , video boyutu

while (camera.isOpened()):
    retrn , video = camera.read()
    if retrn == True : #hakikaten video var mı
        #video = cv2.flip(video , 0) #döndürmak için
        kayit.write(video)
        cv2.imshow('kayit' , video)
        if cv2.waitKey(25) & 0xFF==ord('q') :
            break
camera.release()
kayit.release()
cv2.destroyAllWindows()
