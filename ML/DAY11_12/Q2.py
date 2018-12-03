import numpy as np
import cv2 as cv

img1=cv.imread("ml.png")
img2=cv.imread("opencv-logo.png")

dt=cv.addWeighted(img1,0.7,img2,0.3,0)

cv.imshow("Blend",dt)
cv.waitKey(0)


img1=cv.imread("messi.jpg")
img2=cv.imread("opencv-logo.png")

dt=cv.addWeighted(img1,0.5,img2,0.5,0)

cv.imshow("Blend",dt)
cv.waitKey(0)
