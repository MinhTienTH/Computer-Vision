import numpy as np
import matplotlib.pyplot as plt
import random

#Gán số lượng điểm number_points = 50 và tỉ lệ điểm tối thiểu có trên đường thẳng cần tìm rate = 0.7
number_points = 50
rate = 0.7

#Khởi tạo 2 mảng x và y
multi_x = np.array(np.random.randint(1, 30, number_points))
multi_y = np.array(np.random.randint(1, 30, number_points))

#Khởi tạo mảng y khoảng 70% lượng điểm (70% * 50 = 35 điểm) theo dạng y = 3*x + 5
multi_y[10:45] = 3*multi_x[10:45] + 5

#Chọn toạ độ bất kì của 2 điểm A và B
temp_1 = random.randint(0, number_points - 1)
temp_2 = random.randint(0, number_points - 1)

#Hàm Check_Different_Values
def Check_Different_Values(value_1, value_2, number_points):
    while value_1 == value_2:
        value_2 = random.randint(0, number_points - 1)
        if value_1 != value_2:
            break
    return value_2

#Nếu random trùng nhau thì random lại
if temp_1 == temp_2:
    temp_2 = Check_Different_Values(temp_1, temp_2, number_points)

#Gán toạ độ x,y cho A
x_A = multi_x[temp_1]
y_A = multi_y[temp_1]

#Gán toạ độ x,y cho B
x_B = multi_x[temp_2]
y_B = multi_y[temp_2]

#Tìm toạ độ x,y của vector AB
x_AB = x_B - x_A
y_AB = y_B - y_A

#Tìm hệ số a,b,c của phương trình đường thẳng
a = -y_AB
b = x_AB
c = - a*x_A - b*y_A

#Đếm số lượng điểm thuộc đường thẳng AB
count_point = 0
for i in range(0, number_points, 1):
    if a*multi_x[i] + b*multi_y[i] + c == 0:
        count_point = count_point + 1

#Kiểm tra số lượng điểm trên đường thẳng AB nếu số lượng >= 0.7*n thì vẽ
if count_point >= number_points*rate:
    array_1 = np.array(np.random.randint(0,1,50))
    array_2 = np.array(np.random.randint(0,1,50))

    #Lọc những điểm nào thuộc đường thẳng cần tìm và vẽ
    set_started_index = 0
    for i in range(0, 50, 1):
       if a * multi_x[i] + b * multi_y[i] + c == 0:
          array_1[set_started_index] = multi_x[i]
          array_2[set_started_index] = multi_y[i]
          set_started_index = set_started_index + 1
    plt.scatter(multi_x, multi_y)
    plt.plot(array_1[0:set_started_index], array_2[0:set_started_index], color= "red")
elif count_point < number_points*rate:
    #Kiểm tra lại số lượng điểm có trên đường thẳng AB nếu số lượng < 0.7*n thì chọn lại 2 điểm A và B và tiếp tục
    while count_point < number_points*rate:
       temp_1 = random.randint(0, number_points - 1)
       temp_2 = random.randint(0, number_points - 1)

       if temp_1 == temp_2:
          temp_2 = Check_Different_Values(temp_1, temp_2, number_points)

       x_A = multi_x[temp_1]
       y_A = multi_y[temp_1]

       x_B = multi_x[temp_2]
       y_B = multi_y[temp_2]

       x_AB = x_B - x_A
       y_AB = y_B - y_A
       a = -y_AB
       b = x_AB
       c = -a * x_A - b * y_A

       count_point = 0
       for i in range(0, 50, 1):
         if a * multi_x[i] + b * multi_y[i] + c == 0:
            count_point = count_point + 1;

    #Nếu số lượng điểm đã >= 0.7*n thì vẽ:
    if count_point >= number_points * rate:
        array_1 = np.array(np.random.randint(0, 1, 50))
        array_2 = np.array(np.random.randint(0, 1, 50))

        # Lọc những điểm nào thuộc đường thẳng cần tìm và vẽ
        set_started_index = 0
        for i in range(0, 50, 1):
            if a * multi_x[i] + b * multi_y[i] + c == 0:
                array_1[set_started_index] = multi_x[i]
                array_2[set_started_index] = multi_y[i]
                set_started_index = set_started_index + 1
        plt.scatter(multi_x, multi_y)
        plt.plot(array_1[0:set_started_index], array_2[0:set_started_index], color="r")

#Xuất thông tin phương trình đuường thẳng tìm được
print(f"Phuong trinh duong thang la:{a}*x + {b}*y + {c} = 0")
print(multi_x)
print(multi_y)
plt.show()

