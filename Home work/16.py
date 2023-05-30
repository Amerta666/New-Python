# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

a = True
while a:
    try:
        size_arr = int(input("Сколько элементов в массиве? "))
        if size_arr > 0:
            num = int(input("Какое число искать будем? "))
            if num > 0:
                a = False
            else:
                print("Введите число больше 0")
        else:
            print("Введите число больше '1'")
    except:
        print("Введите ЧИСЛО!")

list_1 = []
count = 0

for i in range(size_arr):
    list_1.append(random.randint(0, 10))
print(list_1)

for i in list_1:
    if i == num:
        count += 1
if count == 0:
    print(f"Число '{num}' не встречается в массиве")
else:
    print(f"Число '{num}' встречается в массиве {count} раз(а)")
