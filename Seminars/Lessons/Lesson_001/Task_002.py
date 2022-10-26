# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


numbers = input('Введите 5 чисел через пробел: ').split()
max_number = int(numbers[0])
for i in numbers:
    if int (i) > max_number:
        max_number = int(i)
print (max_number)