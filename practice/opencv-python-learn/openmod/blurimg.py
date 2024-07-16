import cv2 as cv
img =cv.imread('./imgs/f.jpg')
final_img= cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# so there is more blur which are simple blur and medianblur 
# cv.BORDER_CONSTANT
# cv.BORDER_REPLICATE
# cv.BORDER_REFLECT
# cv.BORDER_WRAP
# cv.BORDER_REFLECT_101
# cv.BORDER_TRANSPARENT
# cv.BORDER_REFLECT101
# cv.BORDER_DEFAULT
# cv.BORDER_ISOLATED
#these are the border availabel for gussianblur 
cv.imshow('main imagee',img)
cv.imshow('final image',final_img)
cv.waitKey(0)
cv.destroyAllWindows()