import cv2

camera = cv2.VideoCapture(0) #kendi kameramsa 0 usb falansa 1

while True:
    retrn , img = camera.read()
    cv2.imshow('Image' , img)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()