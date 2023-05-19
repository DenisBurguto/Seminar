def task45():
    k = int(input('enter k ( k <= 100 000): '))
    test_dict = dict()
    div_sum = 0
    for num in range(k, 0, -1):
        for j in range(int(num ** 0.5), 0, -1):
            if num % j == 0:
                div_sum += j + num // j
        test_dict[num] = div_sum - num
        div_sum = 0
    for num in range(1, k + 1):
        for i in range(num + 1, k):
            if test_dict[num] == i and test_dict[i] == num:
                print(f'{num} {i}')


# task45()


def divisors_sum(num):
    div_sum = 0
    for j in range(int(num ** 0.5), 0, -1):
        if num % j == 0:
            div_sum += j + num // j
    return div_sum


def friendly_nums():
    k = int(input('enter k ( k <= 100 000): '))
    test_dict = dict()
    for num in range(1, k + 1):
        test_dict[num] = divisors_sum(num) - num

    for num1 in range(1, k + 1):
        for num2 in range(num1 + 1, k):
            if test_dict[num1] == num2 and test_dict[num2] == num1:
                print(f'{num1} {num2}')


# friendly_nums()


# Подвиг 7. Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д.
# Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., а значения - список номеров (следующих в том же порядке, что и во входной строке)
# с соответствующими кодами. Полученный словарь вывести командой:
#
# print(*sorted(d.items()))
#
# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])
#

def dic_phones(str_in):
    d = dict()
    list_in = list(str_in.split())

    for el in list_in:
        if el[:2] in d.keys():
            d[el[:2]].append(el)
        else:
            d[el[:2]] = [el]

    print(*sorted(d.items()))


# dic_phones("+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890")


# Задача 4.
# Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив ровно один элемент массива.
# [1, 1, 0,1 ,0 ,1 , 1]
def max_ones(in_list):
    max_one = 0
    one = False
    start = 0
    ind = 0

    for i in range(len(in_list)):
        if in_list[i] == 1 and not one:
            one = True
            start = i
        elif in_list[i] != 1 and one:
            one = False
            if i - start > max_one:
                max_one = i - start
            ind += 1
            start = i
        if start != i:
            max_one = len(in_list) - start

    print(max_one)


# max_ones([0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1])

# Задача 5.
# Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# ［1,4,3,2] => "1-4"
# [1,4] => "1,4"

set_in = {1, 4, 5, 2, 3, 9, 8, 11, 0}


#
# def task5(int_set):
#     sort_list = sorted(list(int_set))
#     out_list = " "
#
#     flag = False
#     for i in range(len(sort_list) - 1):
#         if sort_list[i] + 1 == sort_list[i + 1] and not flag:
#             out_list += str(sort_list[i]) + "-"
#             flag = True
#         elif flag and sort_list[i] + 1 != sort_list[i + 1]:
#             out_list += str(sort_list[i]) + ","
#             flag = False
#         elif not flag and sort_list[i] + 1 != sort_list[i + 1]:
#             out_list += str(sort_list[i]) + ","
#
#     out_list += str(sort_list[-1])
#
#     print(out_list)
#
#
# task5(set_in)

def task5(int_set):
    sorted_set = sorted(int_set)
    ranges = []
    start, end = sorted_set[0], sorted_set[0]
    for num in sorted_set[1:]:
        if num == end + 1:
            end = num
        else:
            ranges.append((start, end))
            print(ranges)
            start = end = num
    ranges.append((start, end))
    print(ranges)

    result = ','.join(str(start) if start == end else f'{start}-{end}' for start, end in ranges)
    print(result)


task5(set_in)
