import cv2
import numpy as np

#Import Image Blood Cells
image_blood = cv2.imread('bloodcell.png', 0)
member , img = cv2.threshold(image_blood, 100, 255, cv2.THRESH_BINARY_INV)

#Create kernel to filter this image
kernel_filter_1 = np.ones((7, 7), np.uint8)
img_erosion = cv2.erode(img, kernel_filter_1, iterations=3)
img_dilation = cv2.dilate(img_erosion, kernel_filter_1, iterations=1)

kernel_filter_2 = np.ones((7, 7), np.uint8)
img_erosion = cv2.erode(img_dilation, kernel_filter_2, iterations=1)

#Result
result = cv2.connectedComponentsWithStats(img_erosion, cv2.CV_32S)
(num_blood_cell, labels, stats, centroids) = result
print('Number of Blood cells: ', num_blood_cell)

cv2.imshow('Result Image Morphology Erosion', img_erosion)
cv2.waitKey(0)