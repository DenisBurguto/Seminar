# Урок 1. Ввод-Вывод, операторы ветвления
# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# #Way1:
# num = int(input("Please input  three-digits positive number: "))
# t = num % 10
# s = (num // 10) % 10
# f = (num // 100) % 10
#
# print('the sum of digits of your number is', f + s + t, f"({f} + {s} + {t})")
#
# #Way2: for any digits positive number:
# num = int(input("Please input   positive number: "))
# sum = 0
# while num != 0:
#     sum += num % 10
#     num //= 10
# print('the sum of digits of your number is', sum)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# num = int(input("Please input  the total quantity of  cranes made: "))
# if num%6 ==0:
#     print(f'Peter made {num//6} cranes , Kate {num//6*4} and Serge same as Peter, {num//6}')
# else:
#     print('incorrect input, the total cranes number must be a multiple of 6')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
#
# 385916 -> yes
# 123456 -> no
# num = int(input("Please input  your ticket 6-digits number to check how lucky you are: "))
# if 100000 <= num <= 999999:
#     print('yes, you are lucky!' if (num // 100000) % 10 + (num // 10000) % 10 + (num // 1000) % 10 ==
#                                    (num // 100) % 10 + (num // 10) % 10 + num % 10 else "no, maybe next time")
# else:
#     print('incorrect input')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no
#
# n = int(input("Please input n- size of chocolate bar: "))
# m = int(input("Please input  m- size of chocolate bar: "))
# k = int(input("How many pieces do you want?  "))
#
# print("yes, it's possible in one division" if (k % n == 0 or k % m == 0) and k <= n * m else "no")
