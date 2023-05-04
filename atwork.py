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


friendly_nums()


