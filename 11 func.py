b = True

def check_fib_pos(A):
    count = 3
    fib_prev = 1
    fib_curr = 1
    fib_next = 1
    while fib_next < A:
        fib_prev = fib_curr
        fib_curr = fib_next
        fib_next = fib_curr + fib_prev
        count +=1
    
    if fib_next == A:
        print("Число", A, "является", count, "-ым числом Фибоначчи")
    else: print("Число", A, "не является числом Фибоначчи и равно -1")
    return count

while b:
	try:
		A = int(input("Введите A: "))
		if A > 1:
			b = False
		else: print("Число А должно быть больше 1!")
	except:
		print("Введите число!")

print(check_fib_pos(A))