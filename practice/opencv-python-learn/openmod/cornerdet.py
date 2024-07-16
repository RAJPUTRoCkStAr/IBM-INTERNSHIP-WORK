# import cv2 as cv

# img = cv.imread('./imgs/soccer_practice.jpg')
# grey_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# final_img = cv.Canny(grey_img,100,100)
# final_img = cv.resize(final_img,(0,0),fx=0.5,fy=0.5)
# cv.imshow('edege detector',final_img)
# cv.waitKey(0)
# cv.destroyAllWindows()


from PIL import Image,ImageFilter
image = Image.open(r"./imgs/soccer_practice.jpg")
image = image.convert("L")
image = image.filter(ImageFilter.FIND_EDGES)
image.save(r"soccer_practice.png")