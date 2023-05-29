# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

import random

a = True
list_1 = []
list_2 = []

while a:
    try:
        n = int(input("Введите кол-во элементов в списке: "))
        if n > 1:
            k = int(input("На сколько элементов необходимо произвести сдвиг? "))
            if n > k > 0:
                a = False
            else:
                print("Введите число от 1 до", n)
        else:
            print("Введите число больше 1")
    except:
        print("Введите число!")

for i in range(n):
    list_1.append(random.randint(0, 10))
print(list_1)

list_2 = list_1[k:] + list_1[:k]
print(list_2)
