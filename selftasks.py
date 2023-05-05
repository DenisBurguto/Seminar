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


# print(simple_or_not(6))


def infected_ref():
    n = int(input('total quantity of refrigerators? '))
    out_string = ""
    test_string = "anton"
    for num in range(n):
        a = input(f"please input string to test for ref with index {num}:  ")
        i = 0
        j = 0
        while i < len(a) and j < len(test_string):
            if a[i] == test_string[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == len(test_string) + 1:
            out_string += str(num) + " "
    print(f"the indexes of infected refrigerators: {out_string}")


# infected_ref()

# task43
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод:    Вывод:
# 1 2 3 2 3    2

def task43():
    import random
    test_list = [random.randint(0, 10) for i in range(0, 10)]
    print(test_list)
    work_list = sorted(test_list)
    pairs = 0
    for ind in range(1, len(work_list)):
        if work_list[ind - 1] == work_list[ind]:
            pairs += 1
    print(pairs)


# task43()

# Задача No45. Решение в группах
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10**5. Программа должна вывести все пары
# дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя
# пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:            Вывод:
# 300            220    284

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
        for i in range(num+1, k):
            if test_dict[num] == i and test_dict[i] == num:
                print(f'{num} {i}')


task45()
