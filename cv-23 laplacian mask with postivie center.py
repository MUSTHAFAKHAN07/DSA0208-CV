import cv2
import numpy as np

img = cv2.imread("C:/Users/musth/OneDrive/Pictures/flower.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.array([[0, 1, 0], [1, 4, 1], [0, 1, 0]])

laplacian = cv2.filter2D(gray, -1, kernel)

sharpened = gray + laplacian

sharpened = cv2.normalize(sharpened, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
