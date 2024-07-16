import numpy as np
import cv2 as cv

img = cv.imread('./imgs/h.png')
img = cv.resize(img,(0,0),fx=0.55,fy=0.55)
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
corner = cv.goodFeaturesToTrack(grey,100,0.01,10)
corner = np.intc(corner)
for corn in corner:
    x,y = corn.ravel()
    cv.circle(img,(x,y),5,(255,0,0),-1)
for i in range(len(corner)):
	for j in range(i + 1, len(corner)):
		corner1 = tuple(corner[i][0])
		corner2 = tuple(corner[j][0])
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
		cv.line(img, corner1, corner2, color, 1)

cv.imshow('chess board', img)
cv.waitKey(0)
cv.destroyAllWindows()