import numpy as np
import cv2 as cv

img1=cv.imread("apple.jpg").astype(np.int8)
img2=cv.imread("orange.jpg").astype(np.int8)

zero_matrix=img1-img1

difference=img2-img1

if ((difference==zero_matrix).all()):
    print("The images are same!")
else:
    print("The images are not same!!")



