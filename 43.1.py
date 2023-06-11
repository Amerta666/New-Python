# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел.
# Все числа списка находятся на разных строках.
#
# Ввод:         Вывод:
# 1 2 3 2 3     2
import random

list_1 = []
list_2 = []
sum = 0

list_1 = list(random.randint(0, 5) for i in range(10))
print(f'Список 1 - {list_1}')
list_2 = list(i for i in list_1)
print((f'Список 2 - {list_2}'))

for i in range(len(list_1)):
    list_2[i] = list_1.count(i)

for i in list_2:
    if i != 0 and i != 1:
        sum = sum + (i // 2)
print(sum)
