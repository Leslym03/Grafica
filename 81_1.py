import cv2 as cv
import numpy as np
import matplotlib.pyplot as plts
from all6 import *
from all7 import *
from all8 import *

path_img1 = 'img/img12.png'
path_img2 = 'img/img13.png'

#output = np.zeros((len(img1),len(img1[0]),3),np.uint8)

#img1 = subtract(path_img1, path_img2, -100)

img1 = divisionC(path_img1, path_img2, 100)

img_new = thresholding_adaptativo(img1, 10, 2)

#img_new = op_and(path_img1, path_img2)
#img_new = op_or(path_img1, path_img2)
#img_new = op_xor(path_img1, path_img2)

cv.imshow ( 'Ejercicio 8.1' , img_new)

if cv.waitKey(0) & 0xff == 27: 
    cv.destroyAllWindows() 
