# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# 5 -> 6


count = 3
fib_prev = 1
fib_curr = 1
fib_next = 1
b = True

while b:
	try:
		A = int(input("Введите A: "))
		if A > 1:
			b = False
		else: print("Число А должно быть больше 1!")
	except:
		print("Введите число!")

while fib_next < A:
	fib_prev = fib_curr
	fib_curr = fib_next
	fib_next = fib_curr + fib_prev
	count +=1
if fib_next == A:
	print("Число", A, "является", count, "по счёту Фибоначчи")
else: print("Число", A, "не является числом Фибоначчи и равно -1")