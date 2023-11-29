import cv2
import numpy as np

source_img = cv2.imread("C:/Users/musth/OneDrive/Pictures/flower.jpg")

source_points = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
destination_points = np.float32([[0, 0], [source_img.shape[1] - 1, 0], [0, source_img.shape[0] - 1], [source_img.shape[1] - 1, source_img.shape[0] - 1]])

A = np.zeros((8, 9))
for i in range(4):
    A[i*2] = [-source_points[i, 0], -source_points[i, 1], -1, 0, 0, 0, source_points[i, 0]*destination_points[i, 0], source_points[i, 1]*destination_points[i, 0], destination_points[i, 0]]
    A[i*2+1] = [0, 0, 0, -source_points[i, 0], -source_points[i, 1], -1, source_points[i, 0]*destination_points[i, 1], source_points[i, 1]*destination_points[i, 1], destination_points[i, 1]]

_, _, Vt = np.linalg.svd(A)
homogeneous_matrix = Vt[-1, :].reshape((3, 3))

transformed_img = cv2.warpPerspective(source_img, homogeneous_matrix, (source_img.shape[1], source_img.shape[0]))

cv2.imshow("Original Image", source_img)
cv2.imshow("Transformed Image", transformed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
