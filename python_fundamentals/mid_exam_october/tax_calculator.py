from math import floor


def family_car_tax(years_taxing, kilometers_passed):
    total_vehicle_tax = 50
    for year in range(1, years_taxing + 1):
        total_vehicle_tax -= 5
    additional_tax_km = floor(kilometers_passed / 3000) * 12
    total_vehicle_tax += additional_tax_km
    return total_vehicle_tax


def heavyDuty_car_tax(years_taxing, kilometers_passed):
    total_vehicle_tax = 80
    for year in range(1, years_taxing + 1):
        total_vehicle_tax -= 8
    additional_tax_km = floor(kilometers_passed / 9000) * 14
    total_vehicle_tax += additional_tax_km
    return total_vehicle_tax


def sports_car_tax(years_taxing, kilometers_passed):
    total_vehicle_tax = 100
    for year in range(1, years_taxing + 1):
        total_vehicle_tax -= 9
    additional_tax_km = floor(kilometers_passed / 2000) * 18
    total_vehicle_tax += additional_tax_km
    return total_vehicle_tax


vehicles_to_be_taxed = input().split('>>')
total_revenue = 0

for vehicle in vehicles_to_be_taxed:
    total_vehicle_tax = 0
    vehicle = vehicle.split()
    vehicle_type, years_taxing, kilometers_passed = vehicle[0], int(vehicle[1]), int(vehicle[2])

    if vehicle_type == 'family':
        total_vehicle_tax = family_car_tax(years_taxing, kilometers_passed)
        print(f"A {vehicle_type} car will pay {total_vehicle_tax:.2f} euros in taxes.")
    elif vehicle_type == 'heavyDuty':
        total_vehicle_tax = heavyDuty_car_tax(years_taxing, kilometers_passed)
        print(f"A {vehicle_type} car will pay {total_vehicle_tax:.2f} euros in taxes.")
    elif vehicle_type == 'sports':
        total_vehicle_tax = sports_car_tax(years_taxing, kilometers_passed)
        print(f"A {vehicle_type} car will pay {total_vehicle_tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")

    total_revenue += total_vehicle_tax

print(f"The National Revenue Agency will collect {total_revenue:.2f} euros in taxes.")