import numpy as np
import cv2 as cv

smile_cascade=cv.CascadeClassifier("haarcascade_smile.xml")
#eye_cascade=cv.CascadeClassifier("haarcascade_eye.xml")

img=cv.imread("group-smiling.jpg")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

smiles=smile_cascade.detectMultiScale(gray,1.6,5)
for (x,y,w,h) in smiles:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #cv.circle(img,(x+(w/2),y+(h/2)),60,(255,0,0),2)

cv.imshow("Smiles",img)
cv.waitKey(0)
