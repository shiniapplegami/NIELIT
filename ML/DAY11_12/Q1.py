import numpy as np
import cv2 as cv
img=cv.imread("gradient.jpg")

ret,dt=cv.threshold(img,127,255, cv.THRESH_BINARY)

cv.imshow("TB",dt)
cv.waitKey(0)
 
ret,dt1=cv.threshold(img,127,255, cv.THRESH_BINARY_INV)

cv.imshow("TBI",dt1)
cv.waitKey(0)


ret,dt2=cv.threshold(img,127,255, cv.THRESH_TRUNC)

cv.imshow("TT",dt2)
cv.waitKey(0)


ret,dt3=cv.threshold(img,127,255, cv.THRESH_TOZERO)

cv.imshow("TTZ",dt3)
cv.waitKey(0)


ret,dt4=cv.threshold(img,127,255, cv.THRESH_TOZERO_INV)

cv.imshow("TTZI",dt4)
cv.waitKey(0)
