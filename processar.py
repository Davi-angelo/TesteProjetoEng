import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("lambo.jpg")

#img_changed = cv.Canny(img, 100, 200) #contorno


#img_changed = cv.GaussianBlur(img,(5,5),0) #Blur


img_changed = cv.resize(img, (200, 200))

#plt.imshow(cv.cvtColor(img_changed, cv.COLOR_BGR2RGB))

plt.subplot(221), plt.imshow(img), plt.title('original') # 3 num: nlinhas, ncolunas, index na matriz

plt.subplot(222), plt.imshow(img_changed),  plt.title('blured')

plt.show()