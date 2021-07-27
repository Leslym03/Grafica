import cv2 as cv
import numpy as np
import matplotlib.pyplot as plts
from all6 import addImage

img1 = cv.imread('img/img1.png')
img2 = cv.imread('img/img2.png')

rows, columns, channels = img1.shape
output = np.zeros((len(img1),len(img1[0]),3),np.uint8)

for i in range(rows):
    for j in range(columns):
        output[i, j] = img1[i,j]/2 + img2[i,j] /2 

#addImage('img/img1.png', 'img/img2.png')

cv.imshow('Ejercicio 1', output)

if cv.waitKey(0) & 0xff == 27: 
    cv.destroyAllWindows() 

