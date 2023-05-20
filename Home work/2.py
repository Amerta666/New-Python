# Найдите сумму цифр трехзначного числа.

#     123 -> 6 (1 + 2 + 3)         100 -> 1 (1 + 0 + 0)

number = input("Введите число: ")
sum = 0

for i in number:
    sum = int(i) + sum
    
print("Сумма цифр числа", number, " = ", sum)




