# 1 – Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


import re
def digit_sum(number):
    return sum(int(dig) for dig in re.findall('\d', number))    

print(digit_sum(input()))

