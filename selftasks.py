# Задача No39. Общее обсуждение
# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел -
# элементы массива. Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12
# (каждое число вводится с новой строки)
# 5 минут
# n = int(input("first array el quantity: "))
# list_one = list(map(int, input(f'Please enter {n} numbers with space: ').split()))
# m = int(input("second array el quantity: "))
# list_two = list(map(int, input(f'Please enter {m} numbers with space: ').split()))
# for el in list_one:
#     print(el if el not in list_two else'', end=' ')

# Задача No41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая
# в данном массиве определит количество элементов, у которых два соседних и,
# при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# Ввод:       Ввод:
# 55
# 1 2 3 4 5   1 5 1 5 1
# Вывод:      Вывод:
# 0           2
# 15 минут
# (каждое число вводится с новой строки)
# n = int(input("array el quantity: "))
# new_list = []
# for _ in range(n):
#     new_list.append(int(input('please input int number: ')))
# print(new_list)
# count = 0
# for i in range(1, len(new_list) - 1):
#     if new_list[i - 1] < new_list[i] > new_list[i + 1]:
#         count += 1
# print(count)

# палиндром или нет рекурсией

def pallindrom_check(s):
    if len(s) == 0:
        return True
    if s[0] != s[-1]:
        return False
    return pallindrom_check(s[1:-1])


# print(pallindrom_check('a rer a'))


# простое ли число рекурсией

def simple_or_not(num, div=None):
    if div is None:
        div = int(num ** 0.5)
    if div < 2:
        return True
    if num % div == 0:
        return False
    return simple_or_not(num, div - 1)


print(simple_or_not(6))


def infected_ref():
    n = int(input('total quantity of refrigerators? '))
    out_string = ""
    test_string = "anton"
    for num in range(n):
        a = input(f"please input string to test for ref with index {num}:  ")
        i = 0
        j = 0
        while i < len(a) and j < 5:
            if a[i] == test_string[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == 5:
            out_string += str(num) + " "
    print(f"the indexes of infected refrigerators: {out_string}")


infected_ref()
