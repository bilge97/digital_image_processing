import cv2
import numpy as np

img = np.zeros((400,400,3) , dtype='uint8' , ) #pixel boyutu 3 renkli olsun , datatype : siyah bir zemin

cv2.rectangle(img , (10,0) , (390,200) , (0,255,0) , 3)
cv2.line(img , (10,0) , (390,200) , (0,0,255) , 3)
cv2.circle(img, (200,350) , 25 , (148,45,4) , 3)

cv2.putText(img , 'Bilge' , (5,300) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 3 , (0,255,255) , 4 , cv2.LINE_4 ) #sol alt köşe yazılır

cv2.imshow('siyah' , img)

cv2.waitKey(0)
cv2.destroyAllWindows()