import numpy as np
import cv2 as cv

img=cv.imread("sudoku.jpg",0)

dt=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

dt1=np.hstack((img,dt))
cv.imshow("ADAPTIVE",dt1)
cv.waitKey(0)
