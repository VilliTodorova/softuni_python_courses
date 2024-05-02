month = input()
nights = int(input())
studio_price_per_night = 0
apartment_price_per_night = 0
studio_discount = 1
apartment_discount = 1

if month == "May" or month == "October":
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if 7 < nights < 14:
        studio_discount = 0.95
    elif nights > 14:
        studio_discount = 0.70
        apartment_discount = 0.90
elif month == "June" or month == "September":
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
    if nights > 14:
        studio_discount = 0.80
        apartment_discount = 0.90
elif month == "July" or month == "August":
    studio_price_per_night = 76.00
    apartment_price_per_night = 77.00
    if nights > 14:
        apartment_discount = 0.90

studio_total = nights * studio_price_per_night * studio_discount
apartment_total = nights * apartment_price_per_night * apartment_discount

print(f"Apartment: {apartment_total:.2f} lv.\nStudio: {studio_total:.2f} lv.")
