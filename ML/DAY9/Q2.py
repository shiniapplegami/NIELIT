import cv2 as cv
import numpy as np

img=np.zeros((512,512,3),np.uint8)

#Drawing Line
cv.line(img,(10,1),(500,100),(0,0,128),2)

cv.line(img,(500,1),(10,100),(0,0,128),2)

cv.imshow("t",img)
cv.waitKey(0)

#Drawing Rectangle

cv.rectangle(img,(10,1),(500,100),(0,128,0),10)

cv.imshow("t",img)
cv.waitKey(0)

