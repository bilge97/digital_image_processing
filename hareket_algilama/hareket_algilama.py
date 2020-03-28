import cv2
from datetime import datetime

def farkImaj(t0 , t1 , t2) :
    fark1 = cv2.absdiff(t2 , t1)#ikisinin farki
    fark2 = cv2.absdiff(t1 , t0)
    return cv2.bitwise_and(fark1 , fark2)
esik_deger = 140000

camera = cv2.VideoCapture(0)

pencereIsmi = "Hareket Algilayici"
cv2.namedWindow(pencereIsmi)

t_eksi = cv2.cvtColor(camera.read()[1] , cv2.COLOR_BGR2GRAY)
t = cv2.cvtColor(camera.read()[1] , cv2.COLOR_BGR2GRAY)
t_arti = cv2.cvtColor(camera.read()[1] , cv2.COLOR_BGR2GRAY)

zamanKontrol = datetime.now().strftime('%Ss')#saniye olarak al zaman bilgisini

while True:
    cv2.imshow(pencereIsmi , camera.read()[1])
    if cv2.countNonZero(farkImaj(t_eksi , t , t_arti)) > esik_deger and zamanKontrol !=datetime.now().strftime('%Ss') :#aynı saniyede foto çekme
        fark_resim = camera.read()[1]
        cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f')+'.jpg' , fark_resim)
    zamanKontrol = datetime.now().strftime('%Ss')  # saniye olarak al zaman bilgisini
    t_eksi = t
    t = t_arti
    t_arti = cv2.cvtColor(camera.read()[1] , cv2.COLOR_BGR2GRAY)
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyAllWindows(pencereIsmi)
        break

