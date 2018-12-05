import numpy as np
import cv2 as cv

img=cv.imread("man.jpg")

kernel=np.ones((2,2),np.uint8)

open1=cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
close=cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)

t=np.hstack((img,open1,close))


cv.imshow("Combined",t)
cv.waitKey(0)
