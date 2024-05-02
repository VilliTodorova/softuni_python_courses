plunder_days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())

gained_plunder = 0

for day in range(1, plunder_days + 1):
    gained_plunder += daily_plunder
    if day % 3 == 0:
        gained_plunder += daily_plunder / 2
    if day % 5 == 0:
        gained_plunder *= 0.7

percentage = (gained_plunder / expected_plunder) * 100

if gained_plunder >= expected_plunder:
    print(f'Ahoy! {gained_plunder:.2f} plunder gained.')
else:
    print(f'Collected only {percentage:.2f}% of the plunder.')
