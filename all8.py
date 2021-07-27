import cv2 as cv
import numpy as np
import matplotlib.pyplot as plts

def thresholding_adaptativo(image, windows_size, constant):
	heigth, width, channels = image.shape

	boundary = int(windows_size/2)

	output = image.copy()

	for x in range(heigth):
	    for y in range(width):

	    	x_i = x-boundary
	    	y_i = y-boundary
	    	x_f = x+boundary
	    	y_f = y+boundary

	    	if x_i<0:
	    		x_i = 0

	    	if x_f>heigth:
	    		x_f = heigth

	    	if y_i<0:
	    		y_i = 0

	    	if y_f>width:
	    		y_f = width

	    	box = image[x_i:x_f, y_i:y_f]					    			

	    	if (image[x][y] < box.mean() - constant).all():
	    		output[x][y] = 0
	    	else:
	    		output[x][y] = 255        

	return output  

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

def op_and(img1_path, img2_path):
    img1 = cv.imread(img1_path)
    img2 = cv.imread(img2_path)
    output = np.zeros((len(img1),len(img1[0]),3),np.uint8)

    img1 = thresholding(img1)
    img2 = thresholding(img2)

    heigth = img1.shape[0]
    width = img1.shape[1]

    for i in range(heigth):
        for j in range(width):
            for k in range(3):
                output[i][j][k] = int(float(img1[i][j][k])) & int(float(img2[i][j][k]))
    return output


def op_or(img1_path, img2_path):
    img1 = cv.imread(img1_path)
    img2 = cv.imread(img2_path)
    output = np.zeros((len(img1),len(img1[0]),3),np.uint8)

    img1 = thresholding(img1)
    img2 = thresholding(img2)

    heigth = img1.shape[0]
    width = img1.shape[1]

    for i in range(heigth):
        for j in range(width):
            for k in range(3):
                output[i][j][k] = int(float(img1[i][j][k])) | int(float(img2[i][j][k]))
    return output


def op_xor(img1_path, img2_path):
    img1 = cv.imread(img1_path)
    img2 = cv.imread(img2_path)
    output = np.zeros((len(img1),len(img1[0]),3),np.uint8)

    img1 = thresholding(img1)
    img2 = thresholding(img2)

    heigth = img1.shape[0]
    width = img1.shape[1]

    for i in range(heigth):
        for j in range(width):
            for k in range(3):
                output[i][j][k] = int(float(img1[i][j][k])) ^ int(float(img2[i][j][k]))
    return output