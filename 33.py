# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
#
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

list_1 = [2, 4, 5, 3, 1, 5]
print(list_1)
def replace(n):
    max_num = n[0]
    min_num = n[0]
    for i in range(len(n)):
        if n[i] > max_num:
            max_num = n[i]
        if n[i] < min_num:
            min_num = n[i]
    if max_num == min_num:
        return print("Все оценки одинаковые")
    for i in range(len(n)):
        if n[i] == max_num:
            n[i] = min_num
    print(f'Минимальная оценка - {min_num}')
    print(f'Максимальная оценка - {max_num}')
    return n

print(replace(list_1))
