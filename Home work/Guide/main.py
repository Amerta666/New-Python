
import os

data_file = 'contacts.txt'
def print_commands():
    return print('Введите интересующую вас команду:'
                 '\n 1 - Показать все записи\n 2 - Поиск\n 3 - Добавить контакт\n 4 - Удалить контакт'
                 '\n 0 - Выход')

def read_data(file):
    with open(file, 'r', encoding="utf-8") as data:
        phone_book = []
        for line in data:
            phone_book.append(line.strip('\n').replace(',', ' '))
    return phone_book

def write_data(file, phone_book):
    with open(file, 'w', encoding="utf-8") as data:
        for line in phone_book:
            data.write(line.replace(' ', ',') + '\n')
        return print('Данные сохранены')


def show_all():
    phone_book = read_data(data_file)
    for line in phone_book:
        print(line)
    return


def search():
    find = input('Введите букву или строку для поиска: ')
    list1 = []
    phone_book = read_data(data_file)
    for line in phone_book:
        if find in line:
            list1.append(line)
    if list1 == []:
        return print("Ничего не найдено, попробуйте ешё раз")
    for line in list1:
        print(line)
    return


def add_record():
    phone_book = read_data(data_file)
    max_num = 0
    for i in phone_book:
        if max_num < int(i[0]):
            max_num = int(i[0])
    print('Добавьте данные')
    number = str(max_num + 1)
    surname = input('Введите фамилию: ')
    name_first = input('Введите имя: ')
    name_second = input('Введите отчество: ')
    phonenumber = input('Введите номер телефона: ')
    n = '\n'
    phone_book.append(str(number) + ',' + str(surname) + ',' + str(name_first) + ',' + str(name_second) + ',' + str(phonenumber))
    write_data(data_file, phone_book)

def del_record():
    del_num = int(input('Введите идентефикатор удаляемой записи: '))
    phone_book = read_data()
    for line in phone_book:
        if line(0) == del_num:
            phone_book.pop(line)
        else: print('Контакт не найден')
    write_data(data_file, phone_book)


clear = lambda: os.system('cls')
clear()
print('Добрый день!')

while True:
    print_commands()
    enter_num = int(input())
    if enter_num == 1:
        show_all()
    elif enter_num == 2:
        search()
    elif enter_num == 3:
        add_record()
    elif enter_num == 4:
        del_record()
    elif enter_num == 0:
        exit()
    else:
        print('ELSE')
