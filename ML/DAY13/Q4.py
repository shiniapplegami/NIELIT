import numpy as np
import cv2 as cv

img=cv.imread("building.png",0)

sobelx=cv.Sobel(img,cv.CV_32F,1,0,ksize=1)
sobely=cv.Sobel(img,cv.CV_32F,0,1,ksize=1)

dt=cv.addWeighted(sobelx,0.5,sobely,0.5,0)

#sobel=cv.Sobel(img,cv.CV_64F,1,1,ksize=1)

cv.imshow("Both",dt)
cv.imshow("Both",sobel)
#cv.imshow("SobelX",sobelx)
#cv.imshow("SobelY",sobely)

cv.waitKey(0)

