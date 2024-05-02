budget = int(input())
season = input()
fishermen_count = int(input())
discount = 1
extra_discount = 1

ship_price = {
    "Spring": 3000,
    "Summer": 4200,
    "Autumn": 4200,
    "Winter": 2600
}

if fishermen_count <= 6:
    discount = 0.9
elif 7 <= fishermen_count <= 11:
    discount = 0.85
elif fishermen_count >= 12:
    discount = 0.75

if fishermen_count % 2 == 0 and season != "Autumn":
    extra_discount = 0.95
else:
    pass

total_price = ship_price[season] * discount * extra_discount
leftover = budget - total_price

if budget >= total_price:
    print(f"Yes! You have {leftover:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(leftover):.2f} leva.")
