#
# 1. Сумма трех
# Посчитайте сумму трех введенных целых чисел
# 2. Площадь
# Пользователь вводит стороны прямоугольника, выведите его площадь
# 3. Одинаковая четность
# Даны два целых числа: A, B. Проверить истинность высказывания: "Числа A и B имеют одинаковую четность".
# 4. Одно положительное
# Даны три целых числа: A, B, C. Проверить истинность высказывания: "Хотя бы одно из чисел A, B, C положительное".
# 5 Меньшее из двух
# Пользователь вводит два целых числа. Выведите меньшее из них.
# 6.Четырехзначное?
# Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, и NO в противном случае.
#

# a = int(input("Ведите первое число: "))
# b = int(input("Ведите второе число: "))
# c = int(input("Ведите третье число: "))
# print("Сумма трех чисел", a+b+c)

# a = int(input("Ведите сторону a: "))
# b = int(input("Ведите сторону b: "))
# print("Площадь прямоугольника ", a*b)

# a = int(input("Ведите первое число: "))
# b = int(input("Ведите второе число: "))
# if a%2==b%2:
#     print(" а и b имеют одинаковую четность")
# else:
#     print(" а и b имеют разную четность")

# a = int(input("Ведите первое число: "))
# b = int(input("Ведите второе число: "))
# c = int(input("Ведите третье число: "))
#
# if a >= 0 or b >= 0 or c >= 0:
#     print("Хотя бы одно число положительно")
# else:
#     print("Ни одно число не положительно")

#
# a = int(input("Ведите первое число: "))
# b = int(input("Ведите второе число: "))
#
# print(a if a < b else b)


# a = int(input("Ведите  число: "))
# print("yes" if a >= 1000 and a <= 9999 else "No")

# Задача No1. Решение в группах
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 Output: 2

# a = int(input("Ведите длинну маршута: "))
# b = int(input("Ведите сколько проезжает машина в день : "))
#
# print("Машина проедит весь путь за ", (a+b-1)//b) // -(-a//b)

#
# Задача No3. Решение в группах
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32
#
# a = int(input("Ведите  число учеников в 1 классе: "))
# b = int(input("Ведите число учеников в 2 классе: "))
# c = int(input("Ведите число учеников в 3 классе: "))
#
# print(-(-a//2 + -b//2 + -c//2))1
#
# Задача No5. Решение в группах
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках) Output: 6
# a = int(input("Введите  порядковый от головы куда он сел : "))
# b = int(input("Введите номер на табличке: "))
#
# if a!=b:
#     print("В поезде количество вагонов", a-1+b )
# else:
#     print("Не достаточно данных")
#
# Задача No7. Решение в группах
# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# Input: 2016 Output: YES
# 15 минут
# a = int(input("Ведите  год для проверки на високосность: "))
# if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
#     print("yes")
# else:
#     print("no")
#
# for _ in range(5): # 0,1,2,3,4
#     print('hello')


# Вводятся числа, пока не введут 0. Найти сумму четных чисел

# a = [1, 2, 3, 4, -5]
# ind = 0
# while x := input() != 0:
#     if a[ind] < 0:
#         print('YES')
#         break
#     ind += 1
# else:
#     print('No')

# Значение переменной-итератера используется
# for i in range(1, 11):
#     print(i ** 2)


# Значение переменной-итератера не используется
# for _ in range(100, 110, 2):  # 0, 1, 2, 3, 4
#     print('HELLO')

# some_list = [-3, 4, 5, 0, 1]
# for a in some_list:
#     print(a)
#
# for ind in range(0, len(some_list)):  # 0, 1, 2, 3, 4
#     print(some_list[ind])


# a = []
# a.append(10)
# print(a)
#
#
# a = []
# print(a)
# a[1] = 200
# a[2] = 300
# print(a)
#
# 9. По11
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно
# является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# 13. 1. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура
# ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
#
# 13. 1. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура
# ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
#
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
#
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
#
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать
# арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый
# арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

import random


# 13. 1. Уставшие от необычно теплой зимы, жители решили
# узнать, действительно ли это самая длинная оттепель за
# всю историю наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая длинная
# оттепель. Оттепелью они называют период, в который среднесуточная
# температура ежедневно превышала 0 градусов Цельсия. Напишите программу,
# помогающую синоптикам в работе.
#
# Пользователь вводит число N – общее количество рассматриваемых
# дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
#
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50
#
#
# days = int(input("Input days count: "))
# countHotDays = 0
# maxCountHotDays = 0
#
# for i in range(1, days + 1):
#     temperature = random.randrange(-50, 51)
#     print(temperature, end= ", ")
#     if temperature > 0:
#         countHotDays += 1
#     else:
#         if maxCountHotDays < countHotDays:
#             maxCountHotDays = countHotDays
#         countHotDays = 0
# print(f"\nDays: {maxCountHotDays}")
# # print(random.randrange(-50, 51))
#
# # Простое число определить
#
# number = int(input("Input number: "))
#
# for i in range(2, int(number ** 0.5) + 1):
#     if number % i == 0:
#         print("Not simple")
#         break
# else:
#      print("Simple")
#
# # if number % 2 != 0 or number % 3 != 0 or number % 5 != 0 or number % 7 != 0:
# #     print("ok")
# # else:
# #     print("not ok")
#     # 2,3,5,7
#
#
#     # number ** 0.5
#
# import random
#
# some_list = []
# for _ in range(10):
#     number = random.randint(1, 10)
#     some_list.append(number)
# print(some_list)
#
# print(some_list.count(7))
#
# print(7 in some_list)

# a = [1, 2, 3]
# b = ['1', '2', '3']
# c = {}
# for ind in range(0, len(a)):
#     c[a[ind]] = b[ind]
# print(c)

# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# some_list = [int(input()) for i in range(5)]
# some_set = set(some_list)
# print(len(some_set))

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
#
# some_list = [int(input()) for i in range(5)]
# print(some_list)
# k = int(input())
# new_list = some_list[k-1:] + some_list[:k-1]
# print(new_list)

# Напишите программу для печати всех уникальных значений в словаре.
#
# some_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "},
#              {" VIII ": " S007 "}]
# # print(type(some_list))
# # print(some_list)
# new_set = set()
# for i in some_list:
#     # new_set.add(*i.values())
#     new_set.add(list(i.values())[0].strip())
#
# print(new_set)

# # Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
#
# import random
#
# some_list = [random.randint(0, 11) for _ in range(5)]
# print(some_list)
# count = 0
# for i in range(1, len(some_list)):
#     if some_list[i] > some_list[i - 1]:
#         count += 1
# print(count)

# 25. Напишите программу, которая принимает на вход строку, и выводит кол-во повторов каждого из символов 1 раз.


# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте. без метода split()
#
# some_str = input()
# some_set = set()
# temp_word = ''
# for letter in some_str:
#     if letter != ' ':
#         temp_word += letter
#     else:
#         if temp_word:
#             some_set.add(temp_word)
#         temp_word = ''
# some_set.add(temp_word)
# print(some_set)
#
# some_str = "wertrtwerewrtewrtwrtwrewr4566464646456456456456456464wrewrw"
# import time
#
# start = time.perf_counter()
# for letter in set(some_str):
#     a = letter, some_str.count(letter)
# end = time.perf_counter()
# duration1 = end - start
# start = time.perf_counter()
# for letter in set(some_str):
#     amount = 0
#     for letter1 in some_str:
#         if letter == letter1:
#             amount += 1
# a = letter, amount
# end = time.perf_counter()
# duration2 = end - start
# print(duration2 / duration1)
#
# import random
#
# some_str = ''.join([chr(random.randint(32, 100)) for _ in range(10 ** 5)])
#
# import time
#
# start = time.perf_counter()
# for letter in set(some_str):
#     a = letter, some_str.count(letter)
# end = time.perf_counter()
# duration1 = end - start
#
# start = time.perf_counter()
# for letter in set(some_str):
#     amount = 0
#     for letter1 in some_str:
#         if letter == letter1:
#             amount += 1
#     a = letter, amount
# end = time.perf_counter()
# duration2 = end - start
# # print(duration2 / duration1)
#
# start = time.perf_counter()
# count = 0
# lens = len(some_str)
# while lens > 0:
#     for i in range(0, lens):
#         if some_str[0] == some_str[i]:
#             count += 1
#     lens -= count
#     a = f'{some_str[0]} -> {count}'
#     some_str = some_str.replace(some_str[0], '')
#     count = 0
# end = time.perf_counter()
# duration3 = end - start
#
# start = time.perf_counter()
# count_dict = {}  # a: 1
# for letter in some_str:
#     if letter not in count_dict:
#         count_dict[letter] = 1
#     else:
#         count = count_dict[letter]
#         count_dict[letter] = count + 1
# end = time.perf_counter()
# duration4 = end - start
# print(duration1, duration2, duration3, duration4)
#

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
#
#
# nums = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(nums)
# print(nums)

# 1) Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# def fibonachi (n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonachi(n - 1) + fibonachi(n - 2)
#
#
# number_N = int(input())
# print(fibonachi(number_N))
#
# def fib(n):
#     if n in (0, 1):
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(7))
#
#
#
#
# # 2)Требуется найти N-е число Фибоначчи
# # Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки
# # на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# def replacement(some_list):
#     min_item = min(some_list)
#     max_item = max(some_list)
#     for i in range(len(some_list)):
#         if some_list[i] == max_item:
#             some_list[i] = min_item
#     return some_list
#
#
# some_list = [random.randint(1, 6) for _ in range(5)]
#
# print(some_list)
# print(replacement(some_list))
#
# some_list = [1, 4, 5, 2, 3, 9, 8, 11, 0]
# flage = True
#
#
# # определить простое число или нет рекурсией
# def simleornot(num, temp=None):
#     if temp == None:
#         temp = num ** 0.5
#         print(temp)
#     while temp >= 2:
#         if num % temp == 0:
#             return False
#         else:
#             return simleornot(num, temp - 1)
#     else:
#         return True
#
#
# print(simleornot(7))
#
#
# def prime(n, d=2):
#     if d * d >= n:
#         # print('prime number')
#         return True
#     elif n == 2:
#         return True
#     elif n % d == 0:
#         # print('not prime')
#         return False
#     else:
#         # print('prime')
#         return prime(n, d + 1)
#
#
# print(prime(57))
#
#
# # палиндром или нет рекурсией
# #
# def palindrome(str):
#     if len(str) < 1:
#         return True
#     else:
#         if str[0] == str[-1]:
#             return palindrome(str[1:-1])
#         else:
#             return False
#
#
# some_str = "абба"
#
# if palindrome(some_str):
#     print("Данная строка палиндром!")
# else:
#     print("Данная строка не палиндром!")
#
#

# Задача No41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# Ввод: Ввод:
# 55
# 1 2 3 4 5 15151
# Вывод: Вывод:
# 02
# 15 минут
# (каждое число вводится с новой строки)
#
# Искусственный
# интеллект
# Антон, созданный
# Гилфойлом, взломал
# сеть
# умных
# холодильников.Теперь
# он
# использует
# их
# в
# качестве
# серверов
# "Пегого дудочника".Помогите
# владельцу
# фирмы
# отыскать
# все
# зараженные
# холодильники.
#
# Для
# каждого
# холодильника
# существует
# строка
# с
# данными, состоящая
# из
# строчных
# букв
# и
# цифр, и
# если
# в
# ней
# присутствует
# слово
# "anton"(необязательно
# рядом
# стоящие
# буквы, главное
# наличие
# последовательности
# букв), то
# холодильник
# заражен
# и
# нужно
# вывести
# номер
# холодильника, нумерация
# начинается
# с
# единицы
#
# Формат
# входных
# данных
# В
# первой
# строке
# подаётся
# число
# n
# n – количество
# холодильников.В
# последующих
# n
# n
# строках
# вводятся
# строки, содержащие
# латинские
# строчные
# буквы
# и
# цифры, в
# каждой
# строке
# от
# 5
# 5
# до
# 100
# 100
# символов.
#
# Формат
# выходных
# данных
# Программа
# должна
# вывести
# номера
# зараженных
# холодильников
# через
# пробел.Если
# таких
# холодильников
# нет, ничего
# выводить
# не
# нужно.
#
# Формат
# входных
# данных
# В
# первой
# строке
# подаётся
# число
# n
# n – количество
# холодильников.В
# последующих
# n
# n
# строках
# вводятся
# строки, содержащие
# латинские
# строчные
# буквы
# и
# цифры, в
# каждой
# строке
# от
# 5
# 5
# до
# 100
# 100
# символов.
#
# Формат
# выходных
# данных
# Программа
# должна
# вывести
# номера
# зараженных
# холодильников
# через
# пробел.Если
# таких
# холодильников
# нет, ничего
# выводить
# не
# нужно.
#
# Sample
# Input
# 1:
# 6
# 222
# anton456
# a1n1t1o1n1
# 0000
# a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample
# Output
# 1:
# 1
# 2
# 3
# Sample
# Input
# 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235
# a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample
# Output
# 2:
# 1
# 2
# 7
# 8
#
# Подвиг 7. Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., а значения - список номеров (следующих в том же порядке, что и во входной строке) с соответствующими кодами. Полученный словарь вывести командой:
#
# print(*sorted(d.items()))
#
# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])
#
# def compress_recursive(string):
#     if len(string) == 0:
#         return []
#     elif len(string) == 1:
#         return [(string, 1)]
#     else:
#         compressed = compress_recursive(string[1:])
#         if string[0] == compressed[0][0]:
#             compressed[0] = (string[0], compressed[0][1] + 1)
#         else:
#             compressed.insert(0, (string[0], 1))
#         return compressed


# values = [1, 23, 42, 'asdfg']
# transformation = lambda x: x
#
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# Задача No49. Общее обсуждение
# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел
# - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные
# выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую
# площадь. Гарантируется, что самая далекая планета ровно одна

#
# def find_farthest_orbit(list_of_orbits):
#     return max(list_of_orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1])
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#
# print(*find_farthest_orbit(orbits))

# Задача No51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики,
# и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same if same_by(lambda x: x % 2, values):
# print(‘same’) else:
# print(‘different’)

def same_by(characteristic, objects):
    return len(list(filter(characteristic, objects))) == len(objects)


test_characteristic = lambda x: x % 2 == 0
values = [0, 2, 101, 6]

if same_by(test_characteristic, values):
    print('same')
else:
    print('different')

# def same_by(characteristic, objects):
#     return len(list(filter(characteristic, objects))) == len(objects)

# # def func(x):
# #     return x % 2 == 0

# function = lambda x: x % 2 == 0
# values = [0, 2, 10, 6]

# if same_by(function, values):
#     print('same')
# else:
#     print('different')
"""
-----------------------------------
"""
# def test(x):
#     def f(n):
#         return n % x == 0
#     return f

# func = test(2)
# print(func(8))

"""
-----------------------------------
"""

some_list = [1,2,3,4]
other_list = ['a', 'b', 'c', 'd']

dict01 = dict(zip(other_list, some_list))

def func01(a, b, c, d):
    return a + b + c + d

# print(func01(**dict01))

def func02(**kwargs):
    print(kwargs)

# func02(a=4, b=7, c=2)

def func03(*args):
    return sum(args)

# print(func03(1,2,3,4,5))

"""
--------------- Defaultdict --------------------
"""

from collections import defaultdict

d = defaultdict(int)
d['a'] += 1
print(d)