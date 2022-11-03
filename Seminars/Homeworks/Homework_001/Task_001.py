# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_number = int(input())
if day_number > 0 and day_number <= 5:
    print('нет')
elif day_number == 6 or day_number == 7:
    print ('да')
elif day_number > 7 or day_number <= 0: 
    print('are you seriously?!?')