import cv2
import numpy as np

image_path = "C:/Users/musth/OneDrive/Pictures/flower.jpg"
original_image = cv2.imread(image_path)

gray_image = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
corner_image = cv2.cornerHarris(gray_image, blockSize = 2, ksize = 3, k = 0.04)
corner_image = cv2.dilate(corner_image,None)

threshold = 0.1* corner_image.max()
corner_image[corner_image < threshold] = 0

original_image[corner_image > 0.01 * corner_image.max()] = [0, 0, 255]
cv2.imshow('image with corners', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
