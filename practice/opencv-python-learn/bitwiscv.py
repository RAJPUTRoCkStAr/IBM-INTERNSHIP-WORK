import cv2 as cv
import numpy as np
img1 = cv.imread('./imgs/b.jpg')
img2 = cv.imread('./imgs/soccer_practice.jpg')
imga2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))
# lets startdoing bitwise operator
andimg = cv.bitwise_and(img1, imga2,mask=None)
orimg = cv.bitwise_or(img1, imga2,mask=None)
xorimg = cv.bitwise_xor(img1, imga2,mask=None)
notimg = cv.bitwise_not(img1, imga2,mask=None)
cv.imshow('and img',andimg)
cv.imshow('or img',orimg)
cv.imshow('xor img',xorimg)
cv.imshow('not img',notimg)
cv.waitKey(0)
cv.destroyAllWindows()