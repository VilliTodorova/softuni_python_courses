film_budget = float(input())
extras_count = int(input())
costume_extra_price = float(input())
film_decor = film_budget * 0.10
COSTUME_DISCOUNT = 0.10    # for over 150 extras

costumes_price = extras_count * costume_extra_price

if extras_count > 150:
    costumes_price = costumes_price * (1 - COSTUME_DISCOUNT)

production_costs = film_decor + costumes_price
leftover = film_budget - production_costs

if leftover >= 0:
    print(f'Action!\nWingard starts filming with {leftover :.2f} leva left.')
else:
    print(f'Not enough money!\nWingard needs {abs(leftover) :.2f} leva more.')
