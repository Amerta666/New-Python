# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
#
# Ввод:  7 2 5
# Вывод: 7 9 11 13 15 | a4(13) = 7 + (4 - 1) * 2

first_num = int(input('Введите первый эл-нт прогрессии: '))
diff = int(input('Введите разность прогрессии: '))
nums = int(input('Введите количество эл-ов прогрессии: '))


list_1 = list((first_num + i * diff) for i in range(nums))
print(list_1)

