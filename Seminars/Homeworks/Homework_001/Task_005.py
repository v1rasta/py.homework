# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#  Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21



xA = float(input('Input А by x: '))
yA = float(input('Input А by y: '))
xB = float(input('Input B by x: '))
yB = float(input('Input B by y: '))

print(round(((xB - xA)**2 + (yB - yA)**2)**(1 / 2), 2))
