# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random

rand_list = []
a = True

while a:
    try:
        n = int(input("Введите кол-во арбузов: "))
        if n > 1:
            a = False
        else:
            print("Введите положительное число больше 1!")
    except:
        print("Введите число!")

for i in range(n):
    rand_list.append(random.randint(1, 9))
print(rand_list)

min_weight = rand_list[0]
max_weight = rand_list[0]

for i in rand_list:
    if i > max_weight:
        max_weight = i
    if i < min_weight:
        min_weight = i

print("Арбуз для тёщи -", min_weight, ", арбуз для себя -", max_weight)
