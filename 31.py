# Последовательностью Фибоначчи называется последовательность чисел
# a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# Input: 7
# Output: 13

def fib(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input('Введите число "n": '))

for i in range(0, n + 1):
    if i == n:
        print(f'{n}-ое число Фибоначчи - "{fib(i)}"')

