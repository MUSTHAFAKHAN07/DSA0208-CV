import cv2
import numpy as np
image = cv2.imread("C:Users/musth/OneDrive/Pictures/cat.jpeg")
img2 = cv2.imread('C:/Users/musth/OneDrive/Pictures/logo.jpeg')

print(image.shape)
cv2.imshow("orginal",image)
imagecopy = image.copy()

cv2.circle(imagecopy,(100,100),30,(255, 0 ,0), -1)
cv2.imshow('image', image)
cv2.imshow('image copy', imageCopy)
cropped_image = image[80:280,150:330]

cv2.imshow("cropped", cropped_image)
cv2.imwrite("cropped image.jpg",cropped_image)
dst = cv2.addWeighted(image, 0.5, img2, 0.7, 0)

img_arr = np.hstack((image, img2))
cv2.imshow('input images',img_arr)
cv2.imshow('blended image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
