import cv2

camera = cv2.VideoCapture(0) #kendi kameramsa 0 usb falansa 1
#camera.set(cv2.CAP_PROP_FRAME_WIDTH , 320)
#camera.set(cv2.CAP_PROP_FRAME_HEIGHT , 320)

while True:
    retrn , img = camera.read()
    griton = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

    #retrn = camera.set(3 , 320) #3. bilgi width 4. bilgi height
    #retrn = camera.set(4, 240)#Bu şekilde de olur
    cv2.imshow('Image' , img)
    cv2.imshow('GriTon', griton)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()