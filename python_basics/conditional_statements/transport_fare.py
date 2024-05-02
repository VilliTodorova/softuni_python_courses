kilometers = int(input())
time_of_day = input()

taxi_initial_fare = 0.70
taxi_per_km_day = 0.79
taxi_per_km_night = 0.90
bus_per_km = 0.09  # for a minimum of 20km distance
train_per_km = 0.06  # for a minimum of 100km distance

taxi_day_price = taxi_initial_fare + kilometers * taxi_per_km_day
taxi_night_price = taxi_initial_fare + kilometers * taxi_per_km_night
bus_price = bus_per_km * kilometers
train_price = train_per_km * kilometers

if kilometers < 20 and time_of_day == 'day':
    print(f'{taxi_day_price :.2f}')
elif kilometers < 20 and time_of_day == 'night':
    print(f'{taxi_night_price :.2f}')
elif 20 <= kilometers < 100:
    print(f'{bus_price :.2f}')
else:
    print(f'{train_price :.2f}')
