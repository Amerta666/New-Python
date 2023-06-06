# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
#
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

string = "a a a b c a a d c d d"
string_2 = string.split()
dict = {}
result = ""

for i in range(len(string_2)):
    if string_2[i] not in dict.keys():
        dict[string_2[i]] = 1
        result += f"{string_2[i]} "
    else:
        result += f"{string_2[i]}_{dict[string_2[i]]} "
        dict[string_2[i]] += 1
print(result)
