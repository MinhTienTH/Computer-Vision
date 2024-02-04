import numpy as np
import cv2

#Read image Background, Foreground and resize them:
#Back Ground
image_background = cv2.imread('Background.png')
image_background = cv2.cvtColor(image_background, cv2.COLOR_BGR2RGB)
image_background = cv2.resize(image_background, (350, 222))

#Fore Ground
image_foreground = cv2.imread('Foreground.png')
image_foreground = cv2.resize(image_foreground, (350, 222))

#Create data before training:
x_bg = image_background.reshape(image_background.shape[0] * image_background.shape[1], 3)
x_fg = image_foreground.reshape(image_foreground.shape[0] * image_foreground.shape[1], 3)

y_bg = np.zeros(x_bg.shape[0])
y_fg = np.zeros(x_fg.shape[0]) + 1

x_train = np.concatenate((x_bg, x_fg))
y_train = np.concatenate((y_bg, y_fg))

#Getting started to train model:
#Import library, I decided to choose SVM model to classify this (C=1e3, gamma= 1e-6)
from sklearn.svm import SVC
model_svm = SVC(C = 1e3, gamma = 1e-6)
print("Getting started to train SVM model...")
model_svm.fit(x_train, y_train)
print("Complete!")

#Testing model:
test_img = cv2.imread('img_test1.png')
h, w, _ = test_img.shape
test_img = test_img.reshape(test_img.shape[0] * test_img.shape[1], 3)

#Predict test image:
predict = model_svm.predict(test_img)
predict = predict.reshape(h, w)

#Remove Background:
result = test_img.reshape(h , w, 3)
for i in range(h):
  for j in range(w):
    if predict[i, j] != 1:
      #Change color background to white:
      result[i, j, :] = 255

#Result Image:
test_img = cv2.imread('img_test1.png')
cv2.imshow("Test Image", test_img)
cv2.imshow("Result Image", result)
cv2.waitKey(0)
