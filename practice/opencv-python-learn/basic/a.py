import cv2
import numpy as np 
img = cv2.imread('./imgs/a.jpg')
width = 1200
height = 450
resized_image = cv2.resize(img, (width, height))

# Rotating the image by 45 degrees
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
rotated_image = cv2.warpAffine(resized_image, rotation_matrix, (width, height))

# Displaying the resized and rotated images
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Rotated Image', rotated_image)



# edges = cv2.Canny(img, 50, 150) #this is to get everyedge of the image

# Displaying the edge-detected image
# cv2.imshow('Edges', edges)
# cv2.imshow('image', img)

# save = cv2.imwrite('withwrite.png',img)
# print("Image written to file-system : ", save)
# pixel = img[100,100]  
# print("These are following pixels of x and y axis",pixel)   

# height = img.shape[0]  
# width = img.shape[1]  
# channels = img.shape[2]  
# dimesions = height*width
# size1 = img.size  
  
# print('Image Dimension    : ',dimesions)  
# print('Image Height       : ',height)  
# print('Image Width        : ',width)  
# print('Number of Channels : ',channels)  
# print('Image Size  :', size1)  

cv2.waitKey(0)  
cv2.destroyAllWindows()