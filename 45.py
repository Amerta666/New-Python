# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести все пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
#
# Ввод:   Вывод:
# 300     220 284

num_k = 300
num1 = 1
num2 = 1
def sum_del(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    return sum

for i in range(2, num_k):
    for j in range(i + 1, num_k):
        num1 = i
        num2 = j
        if sum_del(num1) == num2 and sum_del(num2) == num1:
            print(f'{num1} и {num2}')
