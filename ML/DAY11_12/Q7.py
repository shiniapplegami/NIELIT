import numpy as np
import cv2 as cv

img=cv.imread("messi.jpg",0)

edges=cv.Canny(img,100,200)
edges1=cv.Canny(img,0,100)

img1=np.hstack((img,edges,edges1))
cv.imshow("Edges",img1)
cv.waitKey(0)
