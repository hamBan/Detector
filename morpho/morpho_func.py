import cv2
import numpy as np

def morpho(img):
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(img,kernel,iterations = 1)
    x,y = erosion.shape
    c = 0
    for i in range(x):
        for j in range(y):
            if erosion[i][j]==0:
                c+=1
    return c