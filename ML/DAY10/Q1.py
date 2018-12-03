import numpy as np
import cv2 as cv

img=cv.imread("apple.jpg",0)

rows,cols=img.shape

M=np.float32([[1,0,200],[0,1,100]])

dst=cv.warpAffine(img,M,(cols,rows))

cv.imshow("dt",dst)
cv.waitKey(0)
