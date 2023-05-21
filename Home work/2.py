# Найдите сумму цифр трехзначного числа.

#     123 -> 6 (1 + 2 + 3)         100 -> 1 (1 + 0 + 0)

number = input("Введите число: ")
sum = 0

try: print(int(number) + 1)

except: 
    print("Введите число!")
    exit()

if int(number) < 0:
    print("Введите положительное число!")
    exit()

for i in number:
    sum = int(i) + sum


print("Сумма цифр числа", number, " = ", sum)




