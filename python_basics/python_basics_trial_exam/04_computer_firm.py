computer_models_count = int(input())
last_digit = 0
first_two_digits = 0
sales = 0
total_rating = 0
total_sales = 0
for _ in range(computer_models_count):
    number = int(input())
    last_digit = number % 10
    first_two_digits = number // 10
    rating = last_digit
    possible_sales = first_two_digits
    total_rating += rating
    if rating == 2:
        sales = possible_sales * 0
    elif rating == 3:
        sales = possible_sales * 0.5
    elif rating == 4:
        sales = possible_sales * 0.7
    elif rating == 5:
        sales = possible_sales * 0.85
    elif rating == 6:
        sales = possible_sales * 1

    total_sales += sales

average_rating = total_rating / computer_models_count

print(f"{total_sales :.2f}")
print(f"{average_rating :.2f}")
