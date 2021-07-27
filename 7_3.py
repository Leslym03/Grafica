import cv2 as cv
import numpy as np
import matplotlib.pyplot as plts

def contrastStretching(a,b,c,d,img):
    size = img.shape
    for i in range(size[0]):
        for j in range(size[1]):
            img[i, j] = (img[i,j] - c)*((b-a)/(d-c)) + a
    return img


img1 = cv.imread('img/img7.png')
img2 = cv.imread('img/img8.png')
output = np.zeros((len(img1),len(img1[0]),3),np.uint8)
size = img1.shape

for i in range(size[0]):
    for j in range(size[1]):
        output[i][j] = img1[i][j] / img2[i][j] *100


diff = contrastStretching(0,255,55,141,output)

cv.imshow ( 'Ejercicio 3' , output)

if cv.waitKey(0) & 0xff == 27: 
    cv.destroyAllWindows() 
