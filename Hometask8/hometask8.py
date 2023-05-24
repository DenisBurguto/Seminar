# Урок 8. Работа с файлами
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def work_mode():
    mode = int(input('Please enter 1 for import data or 2 for seek and export: '))
    if mode == 1:
        new_data = [input('please enter surname: '),
                    input('please enter name: '),
                    input('please enter middle name: '),
                    input('please enter phone number: ')]
        imp_data(new_data)
    elif mode == 2:
        key = input('please enter name or surname to search in database: ')
        exp_data(key)

    else:
        print('wrong input')


def imp_data(list_data):
    with open('hometask8.txt', 'a', encoding='utf-8') as file:
        file.write('\n')
        file.write(' '.join(list_data))


def exp_data(key_word):
    with open('hometask8.txt', 'r', encoding='utf-8') as file:
        line = file.readline().split()
        while line:
            for el in line:
                if el.lower() == key_word.lower():
                    print(*line)
                    with open('export.txt', 'a', encoding='utf-8') as out:
                        out.write('\n')
                        out.write(' '.join(line))
            line = file.readline().split()


work_mode()
