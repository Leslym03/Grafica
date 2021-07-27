import cv2 as cv
import numpy as np
import matplotlib.pyplot as plts
from all7 import multiplicationC

img1 = cv.imread('img/img9.png')

rows, columns, channels = img1.shape
output = np.zeros((len(img1),len(img1[0]),3),np.uint8)

for i in range(rows):
    for j in range(columns):
        for k in range(3):
            output[i][j][k] = img1[i][j][k] * 3

multiplicationC('img/img9.png',3)

#cv.imshow('Ejercicio 1' ,output)

if cv.waitKey(0) & 0xff == 27: 
    cv.destroyAllWindows() 
