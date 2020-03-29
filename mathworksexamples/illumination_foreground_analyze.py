import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('NonuniformIlluminationExample_01.png', 0)
kernel = np.ones((10,10), np.uint8)
erosion = cv2.erode(image , kernel , iterations=1) #background
substract_background_image = image - erosion #background removed
_, thr = cv2.threshold(substract_background_image, 50, 255, cv2.THRESH_BINARY) #thresholding
_, connected_components = cv2.connectedComponents(thr)#we find connected component

cv2.imshow('original', image)
#cv2.imshow('erode', erosion)
#cv2.imshow('substracted' , substract_background_image)
#cv2.imshow('threshold', thr)
plt.imshow(connected_components, cmap="nipy_spectral")
plt.show()
cv2.waitKey(0)