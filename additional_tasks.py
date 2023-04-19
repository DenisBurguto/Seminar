import random


# Сложные задачи:
# 1. Создайте список из случайных чисел.
# Найдите номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).

def task1():
    import random
    random_list = [random.randint(-10, 10) for _ in range(10)]
    print(random_list)

    local_max_ind = len(random_list) - 1
    if random_list[-1] > random_list[-2]:
        print(local_max_ind)
    else:
        for i in range(len(random_list) - 2, 1, -1):
            if random_list[i] > random_list[local_max_ind] and random_list[i] > random_list[i - 1]:
                local_max_ind = i
                print(f'last local maximum  is {random_list[i]} with index {i}')
                break


task1()

# 2. Создайте список из случайных чисел.
# Найдите максимальное количество его одинаковых элементов.


# 3. Создайте список из случайных чисел.
# Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2
# 4. Создайте список из случайных чисел.


# Найдите количество различных элементов в нем.
