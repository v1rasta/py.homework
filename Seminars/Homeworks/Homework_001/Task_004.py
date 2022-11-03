# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number_quarter = int(input())
if number_quarter == 1:
    print ('The range in which x > 0 and y > 0')
elif number_quarter == 2:
    print ('The range in which x < 0 and y > 0')
elif number_quarter == 3:
    print ('The range in which x < 0 and y < 0')
elif number_quarter == 4:
    print ('The range in which x > 0 and y < 0')