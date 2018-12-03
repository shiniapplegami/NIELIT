import numpy as np
import cv2 as cv

img=cv.imread("apple.jpg")

rows,cols,a=img.shape

M=cv.getRotationMatrix2D(((cols-1)/2,(rows-1)/2),45,1)

dst=cv.warpAffine(img,M,(cols,rows))

cv.imshow("Rotated_image",dst)
cv.waitKey(0)
