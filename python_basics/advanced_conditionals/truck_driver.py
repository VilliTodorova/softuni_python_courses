season = input()
distance = float(input())
total_earnings = 0

# earnings = {
#     "Season": ["Spring", "Summer", "Autumn", "Winter"],
#     distance <= 5000: [0.75, 0.90, 1.05]
#     5000 < distance <= 10000: [0.95, 1.10, 1.25],
#     10000 < distance <= 20000: 1.45
# }

if season == "Spring" or season == "Autumn":
    if distance <= 5000:
        total_earnings = distance * 0.75
    elif 5000 < distance <= 10000:
        total_earnings = distance * 0.95
    else:
        total_earnings = distance * 1.45
elif season == "Summer":
    if distance <= 5000:
        total_earnings = distance * 0.90
    elif 5000 < distance <= 10000:
        total_earnings = distance * 1.10
    else:
        total_earnings = distance * 1.45
elif season == "Winter":
    if distance <= 5000:
        total_earnings = distance * 1.05
    elif 5000 < distance <= 10000:
        total_earnings = distance * 1.25
    else:
        total_earnings = distance * 1.45

after_tax_income = total_earnings * 4 * 0.90

print(f"{after_tax_income:.2f}")
