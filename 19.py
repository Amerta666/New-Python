# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
import random

# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

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
    list_1.append(random.randint(-50, 50))
print(list_1)

for i in range(len(list_1)):
    if i >= k:
        list_2.append(list_1[i])

for i in range(len(list_1)):
    if i < k:
        list_2.append(list_1[i])

print(list_2)
