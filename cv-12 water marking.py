import cv2
img = cv2.imread("C:Users/musth/OneDrive/Pictures/flower.jpg")
wm = cv2.imread("C:/Users/musth/OneDrive/Pictures/flower.jpg")

h_wm, w_wm = wm.shape[:2]
h_img, w_img = img.shape[:2]

center_x = int(w_img/2)
center_y = int(h_img/2)

top_y = center_y - int(h_wm/2)
left_x = center_x - int(w_wm/2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm

roi = img[top_y:bottom_y,left_x:right_x]
result = cv2.addWeighted(roi, 1, wm, 0.3, 0)
img[top_y:bottom_y,left_x:right_x] = result

cv2.imshow("Watermarked image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
