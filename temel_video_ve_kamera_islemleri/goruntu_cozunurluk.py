import cv2
camera = cv2.VideoCapture(0)

def cozunurluk_1080p():
    camera.set(3 , 1920)
    camera.set(4 , 1080)

def cozunurluk_720p():
    camera.set(3 , 1280)
    camera.set(4 , 720)

def cozunurluk_480p():
    camera.set(3 , 640)
    camera.set(4 , 480)

def cozunurluk_belirle(width , height):
    camera.set(3, width)
    camera.set(4, height)

cozunurluk_1080p()

def skalalama(frame , percent = 75):
    width = int(frame.shape[1] * percent/100 )
    height = int(frame.shape[0] * percent/100 )
    boyut = (width , height)

    return cv2.resize(frame , boyut , interpolation=cv2.INTER_AREA )#dimension

while True:
    retrn , frame = camera.read()
    frame75 = skalalama(frame , 75) #BOYUTLANDIRDIM
    cv2.imshow('Goruntu1 ' , frame)
    cv2.imshow('Goruntu2 ', frame75)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()

