# Дан список чисел. Определите, сколько в нем встречается различных чисел.
#
# [1, 1, 2, 0, -1, 3, 4, 4] -> 6

import random

list_1 = []
list_2 = []
a = True

while a:
    try:
        count = int(input("Введите кол-во элементов в списке: "))
        if count > 1:
            a = False
        else:
            print("Введите число больше 1")
    except:
        print("Введите число!")

for i in range(count):
    list_1.append(random.randint(0, 4))
print(list_1)

for i in range(count):
    if list_1[i] not in list_2:
        list_2.append(list_1[i])

print(list_2)
print("Разных элементов в списке -", len(list_2))
