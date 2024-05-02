# •	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# •	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# •	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# •	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.

from math import pi

shape = input()
area = 0

if shape == 'square':
    square_side = float(input())
    area = square_side ** 2

elif shape == 'rectangle':
    rectangle_side_a = float(input())
    rectangle_side_b = float(input())
    area = rectangle_side_a * rectangle_side_b

elif shape == 'circle':
    radius = float(input())
    area = pi * (radius ** 2)

elif shape == 'triangle':
    triangle_side = float(input())
    triangle_height = float(input())
    area = triangle_height * triangle_side / 2

print(f'{area:.3f}')
