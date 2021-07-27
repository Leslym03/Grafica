import cv2 as cv
import numpy as np
import matplotlib.pyplot as plts

img1 = cv.imread('img/img3.png',1)
img2 = cv.imread('img/img4.png',1)

rows, columns, channels = img1.shape
res = cv.resize(img2, dsize=(columns, rows), interpolation=cv.INTER_CUBIC)
output = np.zeros((len(img1),len(img1[0]),3),np.uint8)

for i in range (len(img1)):
    for j in range (len(img1[i])):
      pixel = []
      for k in range(len(img1[i,j])):
        pixel.append( int((img1[i,j][k]) + int(res[i,j][k]))/2 ) 
      output[i,j] = pixel


cv.imshow ('Ejercicio 2', output)

if cv.waitKey(0) & 0xff == 27: 
    cv.destroyAllWindows() 
