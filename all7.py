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

def multiplicationC(img1_path, c):
    img1 = cv.imread(img1_path)

    rows, columns, channels = img1.shape
    output = np.zeros((len(img1),len(img1[0]),3),np.uint8)

    for i in range(rows):
        for j in range(columns):
            for k in range(3):
                output[i][j][k] = img1[i][j][k] * c

    cv.imshow('multiplication',output)
    cv.waitKey()
    cv.destroyAllWindows()


def divisionI(img1_path, img2_path, constante, intensidad):
    img1 = cv.imread(img1_path)
    img2 = cv.imread(img2_path)
    output = np.zeros((len(img1),len(img1[0]),3),np.uint8)
    rows, columns, channels = img1.shape

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
    return output

def divisionC(img1_path, img2_path, c):
    img1 = cv.imread(img1_path)
    img2 = cv.imread(img2_path)
    output = np.zeros((len(img1),len(img1[0]),3),np.uint8)
    size = img1.shape

    for i in range(size[0]):
        for j in range(size[1]):
            output[i][j] = img1[i][j] / img2[i][j] *c
    return output


def blending(img1_path, img2_path, x):
    img1 = cv.imread(img1_path)
    img2 = cv.imread(img2_path)

    output = np.zeros((len(img1),len(img1[0]),3),np.uint8)

    if img1.shape[0]>img2.shape[0]:
        heigth = img2.shape[0]

    if img1.shape[1]>img2.shape[1]:
        width = img2.shape[1]       

    x=0.25
    for i in range(heigth):
        for j in range(width):
            for k in range(3):
                output[i][j][k] = x*img1[i][j][k] +(1-x)*img2[i][j][k]
    return output
