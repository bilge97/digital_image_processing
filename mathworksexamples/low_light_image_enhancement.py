import cv2
import numpy as np

low_light_image = cv2.imread('LowLightImageEnhancementExample_01.png')
cv2.imshow('low light image', low_light_image)

inverted_image = cv2.bitwise_not(low_light_image)
cv2.imshow('inverted image',inverted_image)

lab= cv2.cvtColor(inverted_image, cv2.COLOR_BGR2LAB)
cv2.imshow("lab",lab)

#IMPORTANT: we wrote the following commands because we couldn't do the histogram equation in colored images

#-----Splitting the LAB image to different channels-------------------------
l, a, b = cv2.split(lab)
cv2.imshow('l_channel', l)
cv2.imshow('a_channel', a)
cv2.imshow('b_channel', b)

#-----Applying CLAHE to L-channel-------------------------------------------
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
cl = clahe.apply(l)
cv2.imshow('CLAHE output', cl) #gray level

#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
limg = cv2.merge((cl,a,b))
cv2.imshow('CLAHE with channels (colored)', limg)

#-----Converting image from LAB Color model to RGB model--------------------
increased_contrast = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
cv2.imshow('contr', increased_contrast)

final = cv2.bitwise_not(increased_contrast)
cv2.imshow('final',final)

cv2.waitKey(0)