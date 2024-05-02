fuel_type = input().casefold().strip()
present_fuel_in_tank = float(input())

if present_fuel_in_tank >= 25:
    if fuel_type == 'gasoline' or fuel_type == 'gas' or fuel_type == 'diesel':
        print(f'You have enough {fuel_type}.')
    else:
        print('Invalid fuel!')
else:
    if fuel_type == 'gasoline' or fuel_type == 'gas' or fuel_type == 'diesel':
        print(f'Fill your tank with {fuel_type}!')
    else:
        print('Invalid fuel!')
