# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

a = True

while a:
    try:
        s = int(input("Введите сумму X и Y: "))
        if 2001 > s > 1:
            p = int(input("Введите произведение X и Y: "))
            if 1000001 > p > 0:
                a = False
            else:
                print("Введите число от 1 до 1000000")
        else:
            print("Введите число от 2 до 2000")
    except:
        print("Введите число!")

for x in range(s+1):
    for y in range(p+1):
        if s == x + y and p == x * y:
            print("Петя загадал числа -", x, "и", y)
            exit()

print("Введённый числа не могут быть одновременно суммой и произведением X и Y")
