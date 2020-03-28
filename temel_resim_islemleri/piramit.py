import cv2
img = cv2.imread('messi.jpg')

up = cv2.pyrUp(img)
down = cv2.pyrDown(img)

cv2.imshow('original' , img)
cv2.imshow('up' , up)
cv2.imshow('down' , down)

cv2.waitKey(0)
cv2.destroyAllWindows()