import cv2
import numpy as np

img = cv2.imread("C:/Users/musth/OneDrive/Pictures/flower.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

unsharp = cv2.GaussianBlur(gray, (0, 0), 3)
unsharp = cv2.addWeighted(gray, 1.5, unsharp, -0.5, 0)

cv2.imshow('Sharpened Image', unsharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
