from math import ceil, floor

grapes_area = int(input())
grapes_kg_per_sq_meter = float(input())
needed_wine_for_sale = int(input())
workers_count = int(input())
liters_wine = 2.5

# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
# От 1 кв.м лозе се изкарват Y килограма грозде. За 1 литър вино са нужни 2,5 кг. грозде.
# Желаното количество вино за продан е Z литра.
# Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно.
# Ако е достатъчно, остатъкът се разделя по равно между работниците на лозето.

grapes_harvest = grapes_area * grapes_kg_per_sq_meter
grapes_for_wine = grapes_harvest * 0.4
wine_produced = grapes_for_wine / liters_wine
leftover_wine = wine_produced - needed_wine_for_sale
wine_per_worker = leftover_wine / workers_count

if wine_produced < needed_wine_for_sale:
    print(f'It will be a tough winter! More {floor(abs(leftover_wine))} liters wine needed.')

else:
    print(f'Good harvest this year! Total wine: {floor(wine_produced)} liters.\n'
          f'{ceil(leftover_wine)} liters left -> {ceil(wine_per_worker)} liters per person.')
# •	Ако произведеното вино е по-малко от нужното:
# “It will be a tough winter! More {недостигащо вино} liters wine needed.”
# Резултатът трябва да е закръглен към по-ниско цяло число
# •	Ако произведеното вино е колкото или повече от нужното:
# “Good harvest this year! Total wine: {общо вино} liters.”
# Резултатът трябва да е закръглен към по-ниско цяло число
# “{Оставащо вино} liters left -> {вино за 1 работник} liters per person.”
# И двата резултата трябва да са закръглени към по-високото цяло число
