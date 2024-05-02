budget = float(input())
ticket_category = input()
fans_count = int(input())

ticket_price = {
    "VIP": 499.99,
    "Normal": 249.99
}

transport_price = 0

if 1 <= fans_count <= 4:
    transport_price = budget * 0.75
elif 5 <= fans_count <= 9:
    transport_price = budget * 0.60
elif 10 <= fans_count <= 24:
    transport_price = budget * 0.50
elif 25 <= fans_count <= 49:
    transport_price = budget * 0.40
elif fans_count >= 50:
    transport_price = budget * 0.25

match_attendance_cost = (fans_count * ticket_price[ticket_category]) + transport_price
leftover = budget - match_attendance_cost

if leftover >= 0:
    print(f"Yes! You have {leftover:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(leftover):.2f} leva.")
