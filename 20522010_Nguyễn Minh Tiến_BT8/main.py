import cv2
import numpy as np

#Buoc 1: Load anh GrayScale
img = cv2.imread("input_img.png", cv2.IMREAD_GRAYSCALE)

#Buoc 2: Tinh histogram
values, count_pixel = np.unique(img, return_counts = True)

#Buoc 3: Tinh tong tich luy CDF
calculate_cdf = np.cumsum(count_pixel)
puzzle = {}
for i in range(len(values)):
    puzzle[values[i]] = round((calculate_cdf[i] - min(calculate_cdf)) / (max(calculate_cdf) - min(calculate_cdf)) * 255)

#Buoc 4: Tinh mapping mau tu anh input sang mau output
equalize_image = img.copy()
for i in range((img.shape[0])):
    for j in range((img.shape[1])):
        equalize_image[i][j] = puzzle[img[i][j]]

#Buoc 5: Hien thi anh
cv2.imshow("Input image",img)
cv2.imshow("Output equalize image", equalize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()