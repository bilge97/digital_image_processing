import cv2
import numpy as np
from matplotlib import pyplot as plt

# In many cases, it is not a good idea.
#in other example adaptive_histogram_eq

image = cv2.imread('pout.tif', 0)
hist_graph_of_image = plt.hist(image, bins='auto')
hist_eq = cv2.equalizeHist(image)

cv2.imshow('hist_eq' , hist_eq)
cv2.imshow('original' , image)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()