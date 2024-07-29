import cv2 as cv
import random as rd
img = cv.imread('main.jpg')
def change_color():
    for i in range(100):
        for j in range(len(img[1])):
            img[i][j] = [rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)]
            return img
# change_color()
def copy_page_img():
    tag= img[400:600,500:550]
    img[200:400, 300:350]=tag
    return img
copy_page_img()
cv.imshow('showing of image',img)
cv.waitKey(0)
cv.destroyAllWindows()