import cv2 as cv
img = cv.imread('main.jpg',-1)
# in im read there are various things like -1=> this is for colorful image
                                        #   0=> this is for blackandwhite imgae
                                        #   1=> this is for real image
img = cv.resize(img,(0,0),fx=0.5,fy=0.5)
# in resise we can resize according to our need use can resize using height and width aur you can do it by giving fx and fy where 0.5 is for half and 2 is 2 times
img = cv.rotate(img,cv.ROTATE_180)
#in rotate we can rotate img according to our need first is cv.ROTATE_90_CLOCKWiSE and second is ROTATE_90 and third is ROTATE_90_COUNTERCLOCKWISE
img = cv.imwrite('firstsaveimage.png',img)
#in imwrite we can save the image according to our need
cv.imshow('showing of image',img)
# in imshow this will show us the image in a new so in string we need to give name of that window and than image you want to see
cv.waitKey(0)
# waitkey is for waiting till this time if it is 0 this means its for infinity
cv.destroyAllWindows()