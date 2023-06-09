# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
#
#
# Input: 2 -> 3 4
# Output: 4 3


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

global i
i = 0
global b
b = len(list_1) - 1
def reverse(n):
    global i
    global b
    if i <= b - 1 // 2:
        a = n[i]
        n[i] = n[b]
        n[b] = a
        i += 1
        b -= 1
        return reverse(n)
    return n

print(reverse(list_1))

