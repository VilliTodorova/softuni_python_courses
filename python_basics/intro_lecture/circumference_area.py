import math

radius = float(input())
circle_area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("{:.2f}\n{:.2f}".format(circle_area, circumference))
