
import cv2
import numpy as np

source_img = cv2.imread("C:/Users/musth/OneDrive/Pictures/flower.jpg")

source_points = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])

angle_degrees = 30
rotation_matrix = cv2.getRotationMatrix2D((source_img.shape[1] // 2, source_img.shape[0] // 2), angle_degrees, 1)
destination_points = cv2.transform(np.array([source_points]), rotation_matrix)[0]

homography_matrix, _ = cv2.findHomography(source_points, destination_points)

transformed_img = cv2.warpPerspective(source_img, homography_matrix, (source_img.shape[1], source_img.shape[0]))

cv2.imshow("Original Image", source_img)
cv2.imshow("Transformed Image", transformed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
