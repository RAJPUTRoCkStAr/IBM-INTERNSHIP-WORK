import cv2
import numpy as np

def affineTransform(img, matrix):
    """
    Apply affine transformation to an image.
    :param img: Input image.
    :param matrix: 2x3 affine transformation matrix.
    :return: Transformed image.
    """
    h, w = img.shape[:2]
    return cv2.warpAffine(img, matrix, (w, h))

# Load an image
img = cv2.imread('media/two.png')

# Define an affine transformation matrix
# Example: rotation by 45 degrees and translation
angle = 45
scale = 1
center = (img.shape[1] // 2, img.shape[0] // 2)
matrix = cv2.getRotationMatrix2D(center, angle, scale)

# Apply the affine transformation
img_transformed = affineTransform(img, matrix)

# Display the original and transformed images
cv2.imshow('Original Image', img)
cv2.imshow('Transformed Image', img_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
