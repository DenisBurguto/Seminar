# Урок 2. Циклы (for, while)
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
#

# heads = 0
# tails = 0
# coins = int(input("Please enter total coins quantity: "))
# for _ in range(coins):
#     side = int(input('heads - 1  or tails -0 ? :'))
#     if side == 1:
#         heads += 1
#     else:
#         tails += 1
#
# print(f"You should return {heads if heads < tails else tails} coins ")
#

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#
# sum= int(input("Please input summ of of two natural numbers : "))
# mult= int(input("Please input multiply of two natural numbers : "))
# #using Vietta theorem, num1 =(sum +sqrt(sum*sum -4*mult))/2 and num2 = (sum -sqrt(sum*sum -4*mult))/2
# print(f"Your hidden numbers are {int((sum +(sum*sum -4*mult)**0.5)/2)} and {int((sum -(sum*sum -4*mult)**0.5)/2)}")


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num_limit = int(input("Please input the limit number : "))
degree = 1
while 2 ** degree <= num_limit:
    print(f"2 in degree {degree} = {2 ** degree}")
    degree += 1
