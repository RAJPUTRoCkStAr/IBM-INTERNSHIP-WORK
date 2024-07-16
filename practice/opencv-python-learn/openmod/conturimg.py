import cv2 as cv
im = cv.imread(r'./imgs/f.jpg')  
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)  
ret, thresh = cv.threshold(imgray, 127, 255, 0)  
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 
final_img = cv.drawContours(im.copy(), contours, -1, (0, 255, 0), 3)
cv.imshow('something',final_img)
cv.waitKey(0)
cv.destroyAllWindows()