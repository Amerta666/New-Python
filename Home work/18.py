# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

a = True

while a:
    try:
        size_arr = int(input("Сколько элементов в массиве? "))
        if size_arr > 0:
            num = int(input("Какое число будем сравнивать? "))
            a = False
        else:
            print("Введите число больше '1'")
    except:
        print("Введите ЧИСЛО!")

list_1 = []

for i in range(size_arr):
    list_1.append(random.randint(-50, 50))
print(*list_1)

diff_curr = None
diff_gen = list_1[0] - num
result = 0


for i in list_1:
    if i == num:
        result = i
        print(f"Заданное число равно элементу - '{result}'")
        exit()
    elif i > num:
        diff_curr = i - num
        if diff_curr < diff_gen:
            diff_gen = diff_curr
            result = i
    elif i < num:
        diff_curr = num - i
        if diff_curr < diff_gen:
            diff_gen = diff_curr
            result = i

print(f"Самый близкий по величине элемент - '{result}'")



