import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png')
img2 = cv2.imread('j2.png')
img3 = cv2.imread('j3.png')

kernel = np.ones((2,2) , np.uint8) # 5 e 5 pixellik alanlarda erosion uygula
erosion = cv2.erode(img2 , kernel , iterations=1) #gürültüyü yokedecek
dilation = cv2.dilate(img3 , kernel , iterations=1)

titles=['original', 'original', 'img2', 'erosion', 'img3', 'dilation']
images=[img, img, img2, erosion, img3, dilation]

for i in range(6):
    plt.subplot(3, 2, i+1), plt.imshow(images[i])
    plt.title(titles[i])
plt.show()

#plt.subplot(321) , plt.imshow(img) , plt.title('original')
#plt.xticks([]) , plt.yticks([])
#plt.subplot(322) , plt.imshow(img) , plt.title('original')
#plt.xticks([]) , plt.yticks([])
#plt.subplot(323) , plt.imshow(img2) , plt.title('img2')
#plt.xticks([]) , plt.yticks([])
#plt.subplot(324) , plt.imshow(erosion) , plt.title('erosion')
#plt.xticks([]) , plt.yticks([])
#plt.subplot(325) , plt.imshow(img3) , plt.title('img3')
#plt.xticks([]) , plt.yticks([])
#plt.subplot(326) , plt.imshow(dilation) , plt.title('dilation')
#plt.xticks([]) , plt.yticks([])

#plt.show()



