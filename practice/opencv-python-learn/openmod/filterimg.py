import cv2 as cv
import numpy as np
img = cv.imread('./imgs/f.jpg')
bilateralFilter_img = cv.bilateralFilter(img,9,75,75) 
cv.imshow('bilateralFilter image',np.hstack((img,bilateralFilter_img)))
boxfilter_img = cv.boxFilter(img, 0, (7,7), img, (-1,-1), False, cv.BORDER_DEFAULT)
cv.imshow('boxFilter image',np.hstack((img,boxfilter_img)))
cv.waitKey(0)()
cv.destroyAllWindows()