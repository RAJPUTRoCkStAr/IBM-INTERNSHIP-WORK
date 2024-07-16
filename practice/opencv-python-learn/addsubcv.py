import cv2 as cv

img = cv.imread('./imgs/b.jpg')
imga = cv.imread('./imgs/soccer_practice.jpg')

imga_resized = cv.resize(imga, (img.shape[1], img.shape[0]))


result = cv.addWeighted(img, 0.5, imga_resized, 0.4, 0)
sub = cv.subtract(img,imga_resized)
cv.imshow('Result', result)
cv.imshow('subtracted', sub)
cv.waitKey(0)
cv.destroyAllWindows()
