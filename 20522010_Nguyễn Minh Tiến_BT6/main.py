from os import remove
import numpy as np
import cv2

image = cv2.imread("nature.png",cv2.IMREAD_UNCHANGED)

print("Giảm kích thước chiều dọc")
print(image.shape)

def Create_Link():
    link = []
    for i in range(image.shape[0]):
        temp = []
        for j in range(image.shape[1]):
            temp.append([i,j])
        link.append(temp)
    link = np.array(link)
    link = [link[0],]
    return link

def Calculate_Nabla(image):
    dx = np.abs(np.diff(image, append = 0, axis = 1))
    dy = np.abs(np.diff(image, append = 0, axis = 0))
    Nabla = np.sqrt(dx**2 + dy**2)
    return Nabla

def Pair(locate):
    column = []
    row = []
    for i in range(len(locate)):
        if i%2 == 0:
            row.append(locate[i])
        else:
            column.append(locate[i])
    return row, column

def findPath(M,path):
    for i in range(1, image.shape[0]):
        list = []
        for j in range(image.shape[1]):
            if j == 0:
                a = min([[i-1,0],np.min(M[i-1,0])],[[i-1,1],np.min(M[i-1,1])],key = lambda x: x[1])
            elif j == image.shape[1] - 1:
                a = min([[i-1,j-1],np.min(M[i-1,j-1])],[[i-1,j],np.min(M[i-1,j])],key = lambda x: x[1])
            else:
                a = min([[i-1,j-1],np.min(M[i-1,j-1])],[[i-1,j],np.min(M[i-1,j]),[[i-1,j+1],np.min(M[i-1,j+1])]],key = lambda x: x[1])
            M[i,j] += a[1]
            cal = np.append(path[a[0][0]][a[0][1]],[i,j],axis = 0)
            list.append(cal)
        path.append(list)
    return path[-1][np.argmin(M[-1][0],axis = 0)]


def Remove_MinEnergy(img, row, column):
    for i in range(len(row)):
        for j in range(len(column)-1):
            if column[j] == 0:
                a = img[i, column[j]+1:,:3][np.newaxis,:,:]
            else:
                a = np.append(img[i,:column[j],:3],img[i,column[j]+1:,:3],axis=0)[np.newaxis,:,:]
        if i == 0:
            new = a.copy()
        else:
            new = np.append(new, a, axis=0)
    img = new.copy()
    return img

cv2.imshow("Initial Image", image)

nabla = Calculate_Nabla(image)

for i in range(20):
    link = Create_Link()
    loc = findPath(nabla, link)
    row, column = Pair(loc)
    image = Remove_MinEnergy(image,row,column)
    nabla = Remove_MinEnergy(nabla,row,column)
    print(image.shape)

print(image.shape)
cv2.imshow("Seam Carving Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
