# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.

class_a = int(input("Введите кол-во учащихся в А классе: "))
class_b = int(input("Введите кол-во учащихся в Б классе: "))
class_c = int(input("Введите кол-во учащихся в В классе: "))

summ_class_a = int(class_a / 2) + int(class_a % 2)
print(summ_class_a)
summ_class_b = int(class_b / 2) + int(class_b % 2)
print(summ_class_b)
summ_class_c = int(class_c / 2) + int(class_c % 2)
print(summ_class_c)

print("Нам нужно приобрести",summ_class_a + summ_class_b + summ_class_c, "парт(ы\у)" )