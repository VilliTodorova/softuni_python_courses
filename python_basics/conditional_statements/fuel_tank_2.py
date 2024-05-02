
GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93
DISCOUNT_CARD_GASOLINE = 0.18
DISCOUNT_CARD_DIESEL = 0.12
DISCOUNT_CARD_GAS = 0.08
DISCOUNT_NO_CARD = 0.00

fuel_type = input().casefold().strip()  # "Gas", "Gasoline" или "Diesel"
fuel_amount = float(input())
club_card = input().casefold().strip()  # yes or no

if club_card == 'yes':
    GASOLINE -= 0.18
    DIESEL -= 0.12
    GAS -= 0.08
else:
    pass

gasoline_price = GASOLINE * fuel_amount
diesel_price = DIESEL * fuel_amount
gas_price = GAS * fuel_amount

if 20 <= fuel_amount <= 25:
    gasoline_price *= 0.92
    diesel_price *= 0.92
    gas_price *= 0.92
elif fuel_amount > 25:
    gasoline_price *= 0.90
    diesel_price *= 0.90
    gas_price *= 0.90
else:
    pass

if fuel_type == 'gasoline':
    print(f'{gasoline_price :.2f} lv.')
elif fuel_type == 'diesel':
    print(f'{diesel_price :.2f} lv.')
elif fuel_type == 'gas':
    print(f'{gas_price :.2f} lv.')
else:
    print('Invalid fuel!')
