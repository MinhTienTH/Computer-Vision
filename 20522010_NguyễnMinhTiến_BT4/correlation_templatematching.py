import cv2
import numpy as np
img = cv2.imread('9-ro.png')
img = cv2.resize(img,(450,500))
template = cv2.imread('template.png')

#Correlation function
def Correlation(temp_img, temp_kernel):
    img_shape = temp_img.shape
    kernel_shape = temp_kernel.shape
    result = cv2.resize(temp_img,(img_shape[1]-kernel_shape[1]+1,img_shape[0]-kernel_shape[0]+1))
    for x in range(0,img_shape[0]-kernel_shape[0]+1):
        for y in range(0,img_shape[1] - kernel_shape[1] + 1):
            result[x,y] = (temp_img[x:x+kernel_shape[0],y:y+kernel_shape[1]]*temp_kernel).sum()/(((temp_img[x:x+kernel_shape[0],y:y+kernel_shape[1]]**2).sum()*(temp_kernel**2).sum()))**0.5
    return result

#Template matching plus correlation function
def TemplateMatching_Correlation(temp_img, temp_kernel):
    max_location = []
    kernel = temp_kernel.copy()
    img_result = temp_img.copy()
    kernel = kernel/255
    img_result = img_result/255
    output = Correlation(img_result, kernel)
    pixel_max = np.array([output.max(), output.max(), output.max()])
    print(output[0:5, 0:5])
    for x in range(0, output.shape[0], 5):
        for y in range(0, output.shape[1], 5):
            if output[x, y, 0] > pixel_max[0]*0.99:
                max_location.append([x, y])
    for rectangle in max_location:
        cv2.rectangle(img_result, (rectangle[1], rectangle[0]), (rectangle[1] + temp_kernel.shape[1], rectangle[0] + temp_kernel.shape[0]), (255, 0, 0), 3)
    return img_result

#Apply function
Image_templatematching_correlation = TemplateMatching_Correlation(img,template)
Image_Result = cv2.resize(Image_templatematching_correlation, (600,900))

#Show image_result
cv2.imshow('Template', template)
cv2.imshow('Image Result', Image_Result)
cv2.waitKey(0)