guests_count = int(input())
plate_price = float(input())
budget = float(input())
discount = 1
cake_price = budget * 0.1

if 10 <= guests_count <= 15:
    discount = 0.85
elif 15 <= guests_count <= 20:
    discount = 0.80
elif guests_count > 20:
    discount = 0.75

total_price = guests_count * plate_price * discount + cake_price
leftover = budget - total_price

if total_price <= budget:
    print(f"It is party time! {leftover :.2f} leva left.")
else:
    print(f"No party! {abs(leftover) :.2f} leva needed.")
