import numpy as np
import cv2 as cv

img=cv.imread("apple.jpg",0)

img=255-img

cv.imshow("Negative_image", img)
cv.waitKey()
