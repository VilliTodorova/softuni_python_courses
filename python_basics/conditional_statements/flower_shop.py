from math import floor, ceil

MAGNOLIA = 3.25
HYACINTH = 4
ROSE = 3.50
CACTUS = 8
TAX = 0.05

magnolias_count = int(input())
hyacinth_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

total_profit = (magnolias_count * MAGNOLIA + hyacinth_count * HYACINTH + roses_count * ROSE + cactus_count * CACTUS)\
               * (1-TAX)
leftover_money = total_profit - gift_price

if total_profit >= gift_price:
    print(f'She is left with {floor(leftover_money)} leva.')
else:
    print(f'She will have to borrow {ceil(abs(leftover_money))} leva.')
