import cv2 as cv
import numpy as np
import matplotlib.pyplot as plts

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

def addImage(img1_path, img2_path):
    img1 = cv.imread(img1_path)
    img2 = cv.imread(img2_path)

    output = np.zeros((len(img1),len(img1[0]),3),np.uint8)
    rows, columns, channels = img1.shape

    for i in range(rows):
        for j in range(columns):
            output[i, j] = img1[i,j]/2 + img2[i,j] /2 

    cv.imshow('addImage',output)
    cv.waitKey()
    cv.destroyAllWindows()


def subtractImage(img1_path, img2_path, c, num_thresholding):
    img1 = cv.imread(img1_path)
    img2 = cv.imread(img2_path)

    output = np.zeros((len(img1),len(img1[0]),3),np.uint8)
    rows, columns, channels = img1.shape

    for i in range(0, rows,1):
        for j in range(0, columns, 1):
            output[i, j] = abs((img1[i][j]/2) - (img2[i][j]/2)) + c

    diff = thresholding(output, num_thresholding)
    return diff


def subtract(img1_path, img2_path, c):
    img1 = cv.imread(img1_path)
    img2 = cv.imread(img2_path)

    output = np.zeros((len(img1),len(img1[0]),3),np.uint8)
    rows, columns, channels = img1.shape

    for i in range(0, rows,1):
        for j in range(0, columns, 1):
            output[i, j] = abs((img1[i][j]/2) - (img2[i][j]/2)) + c

    return output





