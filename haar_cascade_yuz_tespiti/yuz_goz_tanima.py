import cv2

yuz_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
goz_cascade = cv2.CascadeClassifier('haarcascade-eye.xml')

camera = cv2.VideoCapture(0)

while(1):
    _,goruntu = camera.read()
    griton = cv2.cvtColor(goruntu , cv2.COLOR_BGR2GRAY)
    yuzler = yuz_cascade.detectMultiScale(griton , 1.3 , 5)#yüzde 30

    for(x,y,w,h) in yuzler:
        cv2.rectangle(goruntu , (x,y) , (x+w , y+h) , (255,0,0) , 2)
        roi_griton = griton[y:y+h , x:x+w]#region of image yuzun bolgesini dikdortgen olarak aldık
        roi_renkli = goruntu[y:y+h , x:x+w]
        gozler = goz_cascade.detectMultiScale(roi_griton)

        for(ex,ey,ew,eh) in gozler:
            cv2.rectangle(roi_renkli , (ex,ey) , (ex+ew , ey+eh) , (0,158,0) , 2)

    cv2.imshow('goruntu' , goruntu)
    if cv2.waitKey(13) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()