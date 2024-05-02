hall_rent = float(input())

cake_price = hall_rent * 0.2
beverages_price = cake_price * 0.55
entertainer_price = hall_rent / 3

needed_amount = hall_rent + cake_price + beverages_price + entertainer_price

print(needed_amount)
