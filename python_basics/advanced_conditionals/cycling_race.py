junior_cyclists = int(input())
senior_cyclists = int(input())
type_race = input()
money_collected = 0

admission_prices = {
    'group': ['juniors', 'seniors'],
    'trail': [5.50, 7],
    'cross-country': [8, 9.50],
    'downhill': [12.25, 13.75],
    'road': [20, 21.50]
}


# if type_race == "cross-country" and (junior_cyclists + senior_cyclists) >= 50:
#     admission_prices['cross-country'][0] *= 0.25
#     admission_prices['cross-country'][1] *= 0.25

if type_race == "trail":
    money_collected = (junior_cyclists * admission_prices['trail'][0] +
                       senior_cyclists * admission_prices['trail'][1]) * 0.95
elif type_race == "cross-country":
    if (junior_cyclists + senior_cyclists) >= 50:
        admission_prices['cross-country'][0] *= 0.75
        admission_prices['cross-country'][1] *= 0.75
    money_collected = (junior_cyclists * admission_prices['cross-country'][0] +
                       senior_cyclists * admission_prices['cross-country'][1]) * 0.95
elif type_race == 'downhill':
    money_collected = (junior_cyclists * admission_prices['downhill'][0] +
                       senior_cyclists * admission_prices['downhill'][1]) * 0.95
elif type_race == "road":
    money_collected = (junior_cyclists * admission_prices['road'][0] +
                       senior_cyclists * admission_prices['road'][1]) * 0.95

print(f"{money_collected:.2f}")
