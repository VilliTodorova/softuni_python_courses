final_price = 0
price_for_luggage = 0
luggage_over_20_price = float(input())
luggage_weight = float(input())
journey_days = int(input())
luggage_count = int(input())

if luggage_weight < 10:
    price_for_luggage = luggage_over_20_price * 0.2
elif luggage_weight <= 20:
    price_for_luggage = luggage_over_20_price * 0.5
else:
    price_for_luggage = luggage_over_20_price

final_price = price_for_luggage * luggage_count

if journey_days > 30:
    final_price *= 1.1
elif 7 <= journey_days <= 30:
    final_price *= 1.15
elif journey_days < 7:
    final_price *= 1.4

print(f"The total price of bags is: {final_price :.2f} lv.")
