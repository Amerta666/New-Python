# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

# 5 -> 120

n = int(input("Введите n: "))
count = 2
sum = 1
if n == 0:
	print("0! = 1")
elif n == 1:
	print("1! = 1")
elif n < 0:
	print("Введите положительное число!")
	
while count <= n and n > 0:
	sum = sum * count
	count += 1
print(n,"! = ",sum)