import cv2 as cv
import numpy as np 
import matplotlib as plt

def thresholding(img, num):
    size = img.shape
    for i in range(size[0]):
        for j in range(size[1]):
            k = img[i, j]
            if(k[0] < num and k[1] < num and k[2] < num):
                img[i, j] = [255, 255, 255]
            #else:
                #img[i, j] = [0, 0, 0]
    return img

img1 = cv.imread('img/img5.png')
img2 = cv.imread('img/img6.png')
output = np.zeros((len(img1),len(img1[0]),3),np.uint8)
rows, columns, channels = img1.shape

constante = 100 
intensidad = 0 
colores = np.zeros((len(img1),len(img1[0]),3),np.uint8)

for i in range(rows):
    for j in range(columns):
        output[i][j] = (img1[i][j]/img2[i][j]) * constante 

colores = np.sort(output, axis = None)   
lower = int((intensidad/100)*(rows*columns))
higher = int(((100-intensidad)/100)*(rows*columns))
newMin = 0
newMax = 255
Min = int(colores[lower])
Max = int(colores[higher-1])
div = Max-Min
if (div<=0):
    div=1
temp = (newMax-newMin)/div

for x in range(0, rows, 1):
    for y in range(0, columns, 1):
        output[x][y] = (output[x][y] - Min) * temp + newMin


diff = thresholding(output, 60)

cv.imshow ( 'Ejercicio 2' , diff)

if cv.waitKey(0) & 0xff == 27: 
    cv.destroyAllWindows() 

