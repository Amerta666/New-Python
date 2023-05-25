# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе. 
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random

rand_list = []
count = 0
summ = 0
a = True

while a:
    try:
        n = int(input("Введите общее кол-во дней: \n"))
        if 101 > n > 0:
            a = False
        else:
            print("Введите положительное число от 1 до 100!")
    except:
        print("Введите число!")

for i in range(n):
    rand_list.append(random.randint(-50, 50))
print(rand_list)

for i in rand_list:
    if i > 0:
        count += 1
        if count > summ:
            summ = count
    else:
        count = 0
print(summ, "дня(ей) длилась самая длинная оттепель")
