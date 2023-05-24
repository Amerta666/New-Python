count = 2
sum = 1
a = True

while a:
	try:
		n = int(input("Введите n: "))
		if n >= 0:
			a = False
		else: print("Введите положительное целое число!")
	except:
		print("Введите положительное целое число!")

if n == 0:
	print("0 ! = 1")
	exit()
elif n == 1:
	print("1 ! = 1")
	exit()

while n >= count and n > 1:
	sum = sum * count
	count += 1
print(n,"! = ",sum)   