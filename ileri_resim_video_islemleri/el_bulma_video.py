import cv2
import numpy as np
camera = cv2.VideoCapture(0) #kendi kameramsa 0 usb falansa 1
el = cv2.imread('benim_elim.png', 0)
width, height = el.shape[::-1]

while True:
    retrn , img = camera.read()
    griton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(griton, el, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where(res > threshold)
    for n in zip(*loc[::-1]):
        cv2.rectangle(img, n, (n[0] + width, n[1] + height), (0, 255, 255), 1)

    cv2.imshow('Image' , img)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()