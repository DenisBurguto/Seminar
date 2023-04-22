# Урок 5. Рекурсия и алгоритмы
# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def power(a, b):
    if b == 0:
        return 1
    elif b == 1 or a == 1:
        return a
    return power(a, b - 1) * a


# print(power(3, 5))

# Задача 28: https://www.dropbox.com/s/7n18ccc3dgxf8u9/workbook.pdf?dl=0 - задача 6

# Данастрока(возможно,пустая),состоящаяизбукв A-Z:AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB Нужнонаписать функцию RLE, которая
# на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28 И сгенерирует ошибку, если на вход пришла невалидная строка. Пояснения: Если символ встречается
# 1 раз,он остается без изменений; Если символ повторяется более 1 раза ,к нему добавляется количество повторений

def rle_function(input_string):
    import string
    alph = string.ascii_uppercase  # we can create our own string with A-Z instead
    out_str = str()
    count = 1
    for i in range(len(input_string) - 1):
        if input_string[i] in alph:
            if input_string[i] == input_string[i + 1]:
                count += 1
            else:
                out_str += input_string[i]
                if count > 1:
                    out_str += str(count)
                    count = 1
        else:
            return 'invalid string input'
    if input_string[-1] in alph:
        out_str += input_string[-1]
        if count > 1:
            out_str += str(count)
    else:
        return 'invalid string input'
    return out_str


in_str = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
print(rle_function(in_str))
