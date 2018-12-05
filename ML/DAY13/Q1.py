import numpy as np
import cv2 as cv

img=cv.imread("man.jpg")

kernel=np.ones((2,2),np.uint8)

erosion=cv.erode(img,kernel,iterations=2)

dilate=cv.dilate(img,kernel,iterations=2)

#cv.imshow("erode",erosion)
#cv.imshow("dilated",dilate)

dil1=cv.dilate(erosion,kernel,iterations=3)

t=np.hstack((img,erosion,dilate,dil1))

cv.imshow("Combined",t)
cv.waitKey(0)
