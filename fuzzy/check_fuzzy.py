from .fuzzy_func import fuzzy as fz
import numpy as np
import cv2

def check_fuzzy(boxes,image_np,scores):
    height,width,channel=image_np.shape
    area = height*width
    x,y,z = boxes.shape
    s = 0
    counter = 0
    for i in range(y):
        if scores[0][i]>=0.3:
            ymin = int((boxes[0][i][0]*height))
            xmin = int((boxes[0][i][1]*width))
            ymax = int((boxes[0][i][2]*height))
            xmax = int((boxes[0][i][3]*width))
            result = np.array(image_np[ymin:ymax,xmin:xmax])
            gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
            fuzzy = fz(gray)
            s = s+fuzzy
    return s