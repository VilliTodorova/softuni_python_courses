stay_duration = int(input())
facility = input()
rating = input()
discount = 1
rating_price_change = 1

facility_prices = {
    "room for one person": 18.00,
    "apartment": 25.00,
    "president apartment": 35.00
}

if facility == "room for one person":
    pass
elif facility == "apartment":
    if stay_duration < 10:
        discount = 0.70
    elif 10 < stay_duration < 15:
        discount = 0.65
    else:
        discount = 0.50
elif facility == "president apartment":
    if stay_duration < 10:
        discount = 0.90
    elif 10 < stay_duration < 15:
        discount = 0.85
    else:
        discount = 0.80

total_price = (stay_duration - 1) * facility_prices[facility] * discount

if rating == "positive":
    total_price *= 1.25
elif rating == "negative":
    total_price *= 0.90

print(f"{total_price:.2f}")
