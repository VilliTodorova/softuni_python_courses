from math import ceil

guests_count = int(input())
budget = int(input())

easter_bread_bought_count = ceil(guests_count / 3)
eggs_bought_count = guests_count * 2

total_price = easter_bread_bought_count * 4 + eggs_bought_count * 0.45
leftover = budget - total_price

if total_price <= budget:
    print(f"Lyubo bought {easter_bread_bought_count} Easter bread and {eggs_bought_count} eggs.\n"
          f"He has {leftover :.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.\n"
          f"He needs {abs(leftover) :.2f} lv. more.")
