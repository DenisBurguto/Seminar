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
        print(f'last local maximum  is {random_list[-1]} with index {len(random_list) - 1}')
    else:
        for ind in range(len(random_list) - 2, 1, -1):
            if random_list[ind] > random_list[ind + 1] and random_list[ind] > random_list[ind - 1]:
                print(f'last local maximum  is {random_list[ind]} with index {ind}')
                break


# task1()


# 2. Создайте список из случайных чисел.
# Найдите максимальное количество его одинаковых элементов.
def task2():
    import random
    random_list = [random.randint(-10, 10) for _ in range(10)]
    print(random_list)

    max_count = 0
    for num in random_list:
        if random_list.count(num) > max_count:
            max_count = random_list.count(num)

    print("maximum quantity of one same element is ", max_count)


task2()


# 3. Создайте список из случайных чисел.
# Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2
def task3():
    import random
    random_list = [random.randint(-10, 10) for _ in range(10)]
    print(random_list)


# task3()


# 4. Создайте список из случайных чисел.
# Найдите количество различных элементов в нем.
def task4():
    import random
    random_list = [random.randint(-10, 10) for _ in range(10)]
    print(random_list)

# task4()
