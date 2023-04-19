import random


# Сложные задачи:
# 1. Создайте список из случайных чисел.
# Найдите номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).

def task1():
    import random
    random_list = [random.randint(-10, 10) for _ in range(10)]
    print(random_list)

    if random_list[-1] > random_list[-2]:
        print(f'last local maximum  is {random_list[-1]} with index {len(random_list)-1}')
    else:
        for ind in range(len(random_list) - 2, 1, -1):
            if random_list[ind] > random_list[ind+1] and random_list[ind] > random_list[ind - 1]:
                print(f'last local maximum  is {random_list[ind]} with index {ind}')
                break
task1()

# local_max = 0
# N= int(input('Введите количество элементов списка: '))
# spisok = []
#
# for i in range (0,N):
#     spisok.append(random. randint (0, 10))
# print(spisok)
#
# for i in range(1, len (spisok) -1):
#     if spisok[i-1] < spisok[i]> spisok[i+1]:
#             local_max = i
# print(f' Номер ПОСЛЕДНЕГО локального максимума - {local_max+1} и он равен {spisok[local_max]}')


# 2. Создайте список из случайных чисел.
# Найдите максимальное количество его одинаковых элементов.


# 3. Создайте список из случайных чисел.
# Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2
# 4. Создайте список из случайных чисел.


# Найдите количество различных элементов в нем.
