# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива
#
# Ввод:                   Вывод:
# 7                       3 3 2 12
# 3 1 3 4 2 4 12
#
# 6
# 4 15 43 1 15 1
import random

n = int(input('Введите кол-во эл-ов в первом массиве: '))
m = int(input('Введите кол-во эл-ов во втором массиве: '))

list_1 = list(random.randint(0, 20) for i in range(n))
list_2 = list(random.randint(0, 20) for i in range(m))
list_3 = []
print(f'Первый массив - {list_1}')
print(f'Второй массив - {list_2}')

for i in list_1:
    if not i in list_2:
            list_3.append(i)

print(list_3)
