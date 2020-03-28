import numpy as np
import cv2

#CLAHE (Contrast Limited Adaptive Histogram Equalization)

img = cv2.imread('heykel.png',0)

clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imshow('original', img)
cv2.imshow('adaptive histogram eq', cl1)

cv2.waitKey()
cv2.destroyAllWindows()
