import numpy as np
import cv2 as cv

img=cv.imread("opencv-logo.png")

blur=cv.blur(img,(7,7))

cv.imshow("Blur",blur)
cv.waitKey(0)


img=cv.imread("face.jpg")

blur=cv.blur(img,(7,7))

cv.imshow("Blur",blur)
cv.waitKey(0)
