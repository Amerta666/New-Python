# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

list_rand = []
coin_eagle = 0
coin_tails = 0
a = True

while a:
    try:
        n = int(input("Введите кол-во монеток: "))
        if n > 1:
            a = False
        else:
            print("Введите положительное число больше 1!")
    except:
        print("Введите число!")

for i in range(n):
    list_rand.append(random.randint(0, 1))
print(list_rand)

for i in list_rand:
    if i == 0:
        coin_eagle += 1
    else:
        coin_tails += 1

if coin_eagle < coin_tails:
    print("Минимальное число монеток, которое необходимо перевернуть -", coin_eagle)
else:
    print("Минимальное число монеток, которое необходимо перевернуть -", coin_tails)
