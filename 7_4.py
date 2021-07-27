import cv2 as cv
import numpy as np
import matplotlib.pyplot as plts

img1 = cv.imread('img/img3.png')
img2 = cv.imread('img/img9.png')

output = np.zeros((len(img1),len(img1[0]),3),np.uint8)
heigth = img1.shape[0]
width = img1.shape[1]

if img1.shape[0]>img2.shape[0]:
    heigth = img2.shape[0]

if img1.shape[1]>img2.shape[1]:
    width = img2.shape[1]       

x=0.25
for i in range(heigth):
    for j in range(width):
        for k in range(3):
            output[i][j][k] = x*img1[i][j][k] +(1-x)*img2[i][j][k]

cv.imshow ( 'Ejercicio 4' , output)

if cv.waitKey(0) & 0xff == 27: 
    cv.destroyAllWindows() 
