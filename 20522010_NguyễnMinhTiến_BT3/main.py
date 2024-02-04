import cv2
import numpy as np
#Đọc ảnh
Image = cv2.imread('siu.png', 0)

#Đọc kích thước ảnh
print("Kích thước matrix_image:", Image.shape)

filter = np.array([ [1,0.5,1], [0.5,0,-0.5], [-1,-0.5,-1]])

print("Kích thước ma trận filter:", filter.shape)
count = 0
summary = []
#Cross correlation
for i in range(3,Image.shape[0]+1,1):
    h=0
    child = []
    for j in range(3,Image.shape[1]+1,1):
        child.append(Image[count:i,h:j].flatten().dot(filter.flatten()))
        h+=1
    summary.append(child)
    count+=1
image_filter_cross = np.array(summary)
image_filter_cross = image_filter_cross.astype(np.uint8)

#Convolution
filter = np.rot90(np.rot90(filter))
k = 0
total = []
for i in range(3,Image.shape[0]+1,1):
    h=0
    child = []
    for j in range(3,Image.shape[1]+1,1):
        child.append(Image[k:i,h:j].flatten().dot(filter.flatten()))
        h+=1
    total.append(child)
    k+=1
img_filter_cov = np.array(total)
img_filter_cov = img_filter_cov.astype(np.uint8)

#Xuất ảnh gốc, ảnh sau khi convo, ảnh sau khi cross_corr
cv2.imshow('Original Image', Image)
cv2.imshow('Convolution Image', img_filter_cov)
cv2.imshow('Cross Correlation Image', image_filter_cross)
cv2.waitKey(0)