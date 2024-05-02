month = input()  # "march", "april", "may", "june", "july", "august"
hours_spent = int(input())  # >= 5: 50% discount
people_in_group = int(input())  # >= 4: 10% discount
time_of_day = input()  # "day" OR "night"
price_per_hour = 0
discount = 1
extra_discount = 1

if time_of_day == "day":
    if month == "march" or month == "april" or month == "may":
        price_per_hour = 10.50
    elif month == "june" or month == "july" or month == "august":
        price_per_hour = 12.60
elif time_of_day == "night":
    if month == "march" or month == "april" or month == "may":
        price_per_hour = 8.40
    elif month == "june" or month == "july" or month == "august":
        price_per_hour = 10.20

if people_in_group >= 4:
    discount = 0.9
if hours_spent >= 5:
    extra_discount = 0.5

price_after_discounts = (price_per_hour * discount) * extra_discount
total_price = price_after_discounts * people_in_group * hours_spent

print(f"Price per person for one hour: {price_after_discounts :.2f}\n"
      f"Total cost of the visit: {total_price :.2f}")
