import cv2
import numpy as np

img = cv2.imread("schrema.png", cv2.COLOR_BGR2RGB)
background =cv2.imread("bg.png", cv2.COLOR_BGR2RGB)

red_min,green_min,blue_min = np.min(np.min(background, axis = 0), axis=0)
red_max,green_max,blue_max = np.max(np.max(background, axis = 0), axis=0)

img[(img[:,:,0] >= red_min) & (img[:,:,0] <= red_max)] =  0
img[(img[:,:,1] >= green_min) & (img[:,:,1] <= green_max)] =  0
img[(img[:,:,2] >= blue_min) & (img[:,:,2] <= blue_max)] =  0

cv2.imshow("Result",img)
cv2.waitKey(0)
