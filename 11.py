# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# 5 -> 6


count = 3
sum = 1
sum1 = 1
sum2 = 1
b = True

while b:
	try:
		a = int(input("Введите A: "))
		if a > 1:
			b = False
		else: print("Число А должно быть больше 1!")
	except:
		print("Введите число!")

while sum != a and count < 20:
	sum1 = sum2
	sum2 = sum
	sum = sum2 + sum1
	count +=1
	0
if sum == a:
	print("Число", a, "является", count, "по счёту Фибоначчи")
else: print("-1")