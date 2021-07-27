import cv2 as cv
import numpy as np
import matplotlib.pyplot as plts
from all6 import subtractImage

def thresholding(img, num):
    size = img.shape
    for i in range(size[0]):
        for j in range(size[1]):
            k = img[i, j]
            if(k[0] < num and k[1] < num and k[2] < num):
                img[i, j] = [255, 255, 255]
            else:
                img[i, j] = [0, 0, 0]
    return img

img1 = cv.imread('img/img5.png')
img2 = cv.imread('img/img6.png')

rows, columns, channels = img1.shape
res = cv.resize(img2, dsize=(columns, rows), interpolation=cv.INTER_CUBIC)
output = np.zeros((len(img1),len(img1[0]),3),np.uint8)

for i in range(0, rows, 1):
    for j in range(0, columns, 1):
        output[i, j] =  abs((img1[i][j]/2) - (img2[i][j]/2)) - 100

diff = thresholding(output, 169)

subtractImage('img/img5.png', 'img/img6.png', -100, 169)

#cv.imshow('Ejercicio 3', diff)

if cv.waitKey(0) & 0xff == 27: 
    cv.destroyAllWindows() 