import cv2
import numpy as np

img = cv2.imread("C:/Users/musth/OneDrive/Pictures/flower.jpg", cv2.IMREAD_GRAYSCALE)

kernel_size = 5
low_pass_filter = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

low_pass_img = cv2.filter2D(img, -1, low_pass_filter)

scaling_factor = 1.5
high_boost_filter = img - low_pass_img

sharpened_img = img + scaling_factor * high_boost_filter

sharpened_img = np.clip(sharpened_img, 0, 255)

sharpened_img = sharpened_img.astype(np.uint8)

cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
