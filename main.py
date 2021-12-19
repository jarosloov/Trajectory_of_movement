import math
import matplotlib.pyplot as plt
import numpy as np

L = 3
p_lat = [0, 5, 10, 13, 16, 18, 20, 21, 21, 22, 24, 28, 32, 36, 39, 42, 43, 44]  # работающие точки
p_lot = [5, 5, 5, 6, 8, 10, 13, 16, 22, 25, 28, 30, 31, 31, 31, 31, 31, 31]

x = [0, 10, 13, 16, 18, 19, 19, 20, 22, 25, 31, 34, 36, 37, 38, 40, 43, 46, 56, 59, 61, 64, 68, 70]
y = [3,  3,  4,  6,  9, 12, 28, 32, 35, 37, 37, 35, 32, 28, 19, 16, 14, 13, 13, 14, 16, 18, 19, 19]

# p_lat = [0, 5, 10, 13, 16]  # работающие точки
# p_lot = [5, 5, 5, 6, 8]
ksi = []
x_B = []
y_B = []
A = []
B = []

AA = []
BB = []
ksi_2 = []
x_C = []
y_C = []

new_p_lat = []  # x
new_p_lot = []  # y
new_fi = []

# ------------------- Поиск точки B --------------------
# --------------------- Вариант 1 ----------------------

for i in range(len(p_lat) - 1):
    A.append(math.sqrt((p_lat[i] - p_lat[i + 1]) ** 2))
    B.append(math.sqrt((p_lot[i] - p_lot[i + 1]) ** 2))
    if int(A[i]) == 0:
        ksi.append(1.57)  # значение в радианах при угле в 90 градусах
    else:
        ksi.append(round(math.atan(float(B[i]) / float(A[i])), 4))

    x_B.append(p_lat[i] - L * math.cos(ksi[i - 1]))
    y_B.append(p_lot[i] - L * math.sin(ksi[i - 1]))

# ------------------- Поиск точки B --------------------
# --------------------- Вариант 2 ----------------------

#
# speed = 20
# time = 0.01     # 9 секунда в часах 0.00025
#
# pointA = np.array([0, 0])
# distance = 0.
#
# i = 0
# nowTime = 0
#
# lenAllDistance = 0
# lenArray = []
# for i in range(len(p_lat)-1):
#     lenAllDistance += math.sqrt((p_lat[i+1]-p_lat[i])**2 + (p_lot[i+1]-p_lot[i])**2)
#     lenArray.append(math.sqrt((p_lat[i+1]-p_lat[i])**2 + (p_lot[i+1]-p_lot[i])**2))
# print(lenAllDistance)
# print(len(p_lat), len(lenArray))
# while True:
#
#     if i > len(p_lat):
#         break
#     else:
#         if distance > lenAllDistance:
#             break
#         else:
#             distance = speed * nowTime
#             nowDist = distance
#             for i in range(len(lenArray)):
#                 if nowDist > lenArray[i]:
#                     nowDist -= lenArray[i]
#                 else:
#                     print(nowDist)
#
#
#     nowTime +=time
#     #i += 1


# ------------------- Поиск точки С --------------------
# --------------------- Вариант 1 ----------------------


for i in range(len(p_lat) - 2):
    AA.append(math.sqrt((x_B[i] - x_B[i + 1]) ** 2))
    BB.append(math.sqrt((y_B[i] - y_B[i + 1]) ** 2))
    if int(AA[i]) == 0:
        ksi_2.append(1.57)  # значение в радианах при угле в 90 градусах
    else:
        ksi_2.append(round(math.atan(float(BB[i]) / float(AA[i])), 4))

    x_C.append(x_B[i] - L * math.cos(ksi_2[i - 1]))
    y_C.append(y_B[i] - L * math.sin(ksi_2[i - 1]))


# ------------------- Поиск точки С --------------------
# --------------------- Вариант 2 ----------------------

# Bm = 1
#
# for i in range(len(p_lat) - 2):
#
#     ksi_2.append(round(math.atan(6000*x_B[i]/(42000 * x_B[i])), 4))
#
#     x_C.append(x_B[i] + Bm * math.sin(ksi_2[i - 1]))
#     y_C.append(y_B[i] - Bm * math.cos(ksi_2[i - 1]))


# --------------------- Поиск угла ---------------------

def AngleSearch(x_1, y_1, x_2, y_2):
    aLen = math.fabs(x_1 - x_2)
    bLen = math.fabs(y_1 - y_2)
    if int(aLen) == 0:
        return 1.57
    else:
        return round(math.atan(bLen / aLen), 4)


# --------------------- Дробление --------------------- (нет смысла)

def FragmentationArea(x_1, y_1, x_2, y_2, lenFragmentation):
    number = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) / float(lenFragmentation)
    if number != 0:
        aLen = math.fabs(x_1 - x_2) / number
        bLen = math.fabs(y_1 - y_2) / number
        # new_p_lat.append(x_1)
        # new_p_lot.append(y_1)
        for i in range(round(number) - 1):
            new_p_lat.append(new_p_lat[-1] + aLen)
            new_p_lot.append(new_p_lot[-1] + bLen)
    else:
        print("Ошибка")


# ----------------- Рисование графика ------------------

plt.plot(p_lat, p_lot, label='output')
plt.plot(x_B, y_B, 'o-', label='back axle')
# plt.plot(x_B, y_B, )
plt.plot(x_C, y_C, 'o-', label='trailer')

plt.legend()
plt.show()
