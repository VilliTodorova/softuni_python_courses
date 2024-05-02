flower_type = input()   # "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"
flower_count = int(input())
budget = int(input())
discount = 1

flower_price = {
    "Roses": 5.00,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3.00,
    "Gladiolus": 2.50
}
if flower_type == "Roses" and flower_count > 80:
    discount = 0.9
elif flower_type == "Dahlias" and flower_count > 90:
    discount = 0.85
elif flower_type == "Tulips" and flower_count > 80:
    discount = 0.85
elif flower_type == "Narcissus" and flower_count < 120:
    discount = 1.15
elif flower_type == "Gladiolus" and flower_count < 80:
    discount = 1.20

total_price = flower_count * flower_price[flower_type] * discount
leftover = budget - total_price
if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {leftover:.2f} leva left.")
else:
    leftover = total_price - budget
    print(f"Not enough money, you need {leftover:.2f} leva more.")
