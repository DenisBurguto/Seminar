# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
def task22():
    one = int(input('Please enter first set lens: '))
    two = int(input('Please enter second set lens: '))
    # list_one = []
    # list_two = []
    #
    # for i in range(one):
    #     list_one.append(int(input(f'enter {i + 1} element of first list: ')))
    #
    # for j in range(two):
    #     list_two.append(int(input(f'enter {j + 1} element of second list: ')))
    #
    # set_out = sorted(set(list_one + list_two))
    # print(set_out)
    # print(type(set_out))

    set_one = set()
    set_two = set()
    for i in range(one):
        set_one.add(int(input(f'enter {i + 1} element of first set: ')))

    for j in range(two):
        set_two.add(int(input(f'enter {j + 1} element of second set: ')))

    print(set(sorted(set_one | set_two)))


# task22()


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

def task25():
    import random
    n = int(input('Please enter N - quantity of plants: '))
    plant_dict = dict()
    for i in range(1, n + 1):
        plant_dict[i] = random.randint(0, 100)  # quantity of strawberries on each plant or take it from inputed list instead of random
    print(plant_dict)
    max_strawberries = plant_dict[1] + plant_dict[n] + plant_dict[2]
    key = 1
    for i in range(2, n):
        if plant_dict[i] + plant_dict[i - 1] + plant_dict[i + 1] > max_strawberries:
            max_strawberries = plant_dict[i] + plant_dict[i - 1] + plant_dict[i + 1]
            key = i

    print(f' max possible harvest in one operation is  {max_strawberries} strawberries, central plant is {key}')


task25()
