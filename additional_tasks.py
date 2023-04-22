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


# task2()


# 3. Создайте список из случайных чисел.
# Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2
def task3():
    import random
    random_list = [random.randint(-10, 100) for _ in range(10)]
    print(random_list)

    first_max = max(random_list)
    random_list.remove(first_max)
    print("second maximum in the list is", max(random_list))


# task3()


# 4. Создайте список из случайных чисел.
# Найдите количество различных элементов в нем.
def task4():
    import random
    random_list = [random.randint(-10, 10) for _ in range(20)]
    print(random_list)

    print("total quantity of different items in list  is", len(set(random_list)), "from", len(random_list))


# task4()

# Задача 1.
# Напишите функцию, которая переворачивает строку.

# def string_reverse(string):
#     new_str = str()
#     for i in range(len(string) - 1, -1, -1):
#         new_str += string[i]
#     return new_str
#
#
# s = input("initial string? :")
# print((string_reverse(s)))

# Задача 2.
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3] (порядок неважен)
#
list1 = [1, 2, 3, 2, 0]
list2 = [5, 1, 2, 7, 3, 2, 2]
dict1 = dict()
for el in list1:
    dict1[el] = list1.count(el)

result = []
for el in list2:
    if dict1.get(el) is not None and dict1.get(el) != 0:
        result.append(el)
        dict1[el] = dict1[el] - 1

print(result)

# list_out = []
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] == list2[j]:
#             list_out.append(list1[i])
#             list2.pop(j) #list2[j] = ''
#             break
# print(list_out)


# Задача 3.
# Sample Input
# ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
#

list_in = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac"]


def list_letters(input_list):
    temp_dict = dict()
    for string in list_in:
        temp_dict[string] = sorted(string)
    ind = 1
    temp_ind = 1
    for i in range(len(list_in)): #grouping words with same letters
        for j in range(ind, len(list_in)):
            if sorted(list_in[i]) == temp_dict[list_in[j]]:
                temp = list_in[temp_ind]
                list_in[temp_ind] = list_in[j]
                list_in[j] = temp
                temp_ind += 1
                ind += 1
    ind = 0
    temp_list = []
    list_out = []
    for i in range(len(list_in)): #formatting output in internal lists
        if sorted(list_in[i]) == temp_dict[list_in[ind]]:
            temp_list.append(list_in[i])
        else:
            list_out.append(temp_list)
            ind = i
            temp_list = [list_in[i]]
    list_out.append(temp_list)
    return list_out


print(list_letters(list_in))
