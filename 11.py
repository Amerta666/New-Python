# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# 5 -> 6

a = int(input("Введите A: "))
count = 3
sum = 1
sum1 = 1
sum2 = 1

if a == 0 or a == 1 or a < 0:
	print("Число А должно быть больше 1!")
	exit()

while sum != a and count < 20:
	sum1 = sum2
	sum2 = sum
	sum = sum2 + sum1
	count +=1
	0
if sum == a:
	print("Число", a, "является", count, "по счёту Фибоначчи")
else: print("-1")