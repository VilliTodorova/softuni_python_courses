car_data = tuple([car for car in input().split(', ')] for _ in range(int(input())))

cars_inside = set()

for car in car_data:
    if car[0] == "IN":
        cars_inside.add(car[1])
    else:
        cars_inside.remove(car[1])
if cars_inside:
    print("\n".join(cars_inside))
else:
    print("Parking Lot is Empty")
