import math

budget = float(input())
flour_price = float(input())  # 1kg pack per loaf
eggs_price = flour_price * 0.75  # 1 pack per loaf
milk_price = flour_price * 1.25  # 0.250ml per loaf
loaf_price = flour_price + eggs_price + milk_price / 4
bread_count = int(math.floor(budget / loaf_price))
leftover_budget = budget - (bread_count * loaf_price)

eggs_collected = 0
current_loaf_count = 0

for loaf in range(bread_count):
    current_loaf_count += 1
    eggs_collected += 3
    if current_loaf_count % 3 == 0:
        eggs_collected -= (current_loaf_count - 2)

print(f"You made {bread_count} loaves of Easter bread! Now you have {eggs_collected} eggs and {leftover_budget:.2f}BGN left.")
