# Урок 6. Повторение списков
# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с
# клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
#
def task30():
    start = int(input("first element? : "))
    path = int(input('path? : '))
    elements = int(input("element's quantity? : "))

    my_list = [el for el in range(start, start + path * elements, path)]
    print(my_list)


# task30()


# Задача 32: Определить индексы элементов массива (списка), значения
# которых принадлежат заданному диапазону (т.е. не меньше заданного
# минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4,-2,10,2,0,-9,8,10,-9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


def task32(list_in):
    min_mun = int(input('minimun? : '))
    max_mun = int(input('maximum? : '))
    list_out = [ind for ind in range(len(list_in)) if min_mun <= list_in[ind] <= max_mun]
    return list_out

print(task32([-5, 9, 0, 3, -1, -2, 1, 4,-2,10,2,0,-9,8,10,-9, 0, -5, -5, 7]))
