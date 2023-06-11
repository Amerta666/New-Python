

# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
#
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

min_num = int(input('Введите минимальное значение: '))
max_num = int(input('Введите максимальное значение: '))

list_1 = list(random.randint(-20, 30) for i in range(random.randint(10, 15)))
list_2 = []
print(f'Список - {list_1}')

for i in range(len(list_1)):
    if max_num >= list_1[i] >= min_num:
        list_2.append(i)

print(f'Индексы элементов заданного диапазона - {list_2}')