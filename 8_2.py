import cv2 as cv
import numpy as np
import matplotlib.pyplot as plts

img1 = cv.imread('img/img10.png')
img2 = cv.imread('img/img11.png')

output = np.zeros((len(img1),len(img1[0]),3),np.uint8)

def thresholding(img):
	heigth = img.shape[0]
	width = img.shape[1]

	for x in range(heigth):
	    for y in range(width):
	        color = img[x][y]
	        if (140 > color).all():
	        	img[x][y] = 255
	        else:
	        	img[x][y] = 0        		  	              	
	return img


img1 = thresholding(img1)
img2 = thresholding(img2)

heigth = img1.shape[0]
width = img1.shape[1]

for i in range(heigth):
    for j in range(width):
        for k in range(3):
            output[i][j][k] = int(float(img1[i][j][k])) | int(float(img2[i][j][k]))

cv.imshow ( 'Ejercicio 1' , output)

if cv.waitKey(0) & 0xff == 27: 
    cv.destroyAllWindows() 
