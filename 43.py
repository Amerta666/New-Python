# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел.
# Все числа списка находятся на разных строках.
#
# Ввод:         Вывод:
# 1 2 3 2 3     2
import random

list_1 = list(random.randint(0, 10) for i in range(random.randint(5, 11)))
print(list_1)

list_2 = []

count = 0
for i in range(len(list_1) - 1):
    j = i + 1
    while j < len(list_1):
        if list_1[i] == list_1[j]:
            count += 1
        j += 1

print(count)
