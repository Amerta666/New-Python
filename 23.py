# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
#
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
import random

list_1 = []
list_2 = []
count = 0

size_array = int(input("Введите кол-во элементов списка: "))

for i in range(size_array):
    list_1.append(random.randint(-50, 50))
print(list_1)

for i in range(len(list_1) - 1):
    if list_1[i] < list_1[i + 1]:
        list_2.append(list_1[i])
        list_2.append(list_1[i + 1])
        count += 1
print(list_2)
print(count)