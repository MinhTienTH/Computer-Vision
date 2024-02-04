import cv2
import numpy as np


def deg2grad(deg):
    return deg * 3.141592654 / 180


# Step 0.5: initialize hough table
theta_range = np.arange(-3.14, 3.14, 0.01)
H = np.zeros((520 * 2 + 1, len(theta_range)), dtype=np.uint8)

# Step 1: accumulate hough space
list_theta = []


def accumulate(point):
    # for theta in range(360):
    for theta in theta_range:
        pro = point[0] * np.cos(theta) + point[1] * np.sin(theta)
        # If pro in range of Hough space
        if pro >= 0 and pro < 520 * 2 + 1:
            # map theta to Hough space
            # (theta - (-3.14))/0.01
            H[int(pro), int((theta + 3.14) / 0.01)] += 1
            list_theta.append([int(pro), int((theta + 3.14) / 0.01)])
    return H


def detect_line():
    H_list = []
    for list in list_theta:
        if H[list[0], list[1]] > 140:
            H_list.append([list[0], list[1]])

    for i in range(len(H_list)):
        H_list[i][1] = (H_list[i][1]) * 0.01 - 3.14

    return H_list


#Read image
image = cv2.imread('football_yard.png', cv2.IMREAD_COLOR)

#Convert color to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Edge_canny image
edge = cv2.Canny(gray_image, 500, 650, apertureSize=3)

squeeze_arr = np.squeeze(cv2.findNonZero(edge))
for i in range(len(squeeze_arr)):
    accumulate(squeeze_arr[i])

summary_line = detect_line()
for line in summary_line:
    rho, theta = line[0], line[1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("Result Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()








