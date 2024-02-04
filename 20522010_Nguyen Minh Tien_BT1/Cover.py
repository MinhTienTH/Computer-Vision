import cv2
import os
#Read Image
img_1 = cv2.imread(r'Oggy.png')
img_2 = cv2.imread(r'Dora.png')
#Display Image:
cv2.imshow("First Picture",img_1)
cv2.imshow("Second Picture",img_2)
cv2.waitKey(0)
#Get size Image:
h_1,w_1,c_1 = img_1.shape
h_2,w_2,c_2 = img_2.shape

#Save min height and width from between two images:
height = min(h_1,h_2)
width = min(w_1,w_1)
img_1 = cv2.resize(img_1,(width,height))
img_2 = cv2.resize(img_2,(width,height))
Speed = 5
for D in range(0,width+1,Speed):
    result=img_1.copy()
    result[:,D:width,:] = img_1[:,D:width,:]
    result[:,width-D:width,:] = img_2[:,width-D:width,:]
    cv2.imshow("Cover",result)
    cv2.waitKey(10)