budget = float(input())
season = input()
destination = ""
stay_type = ""
vacation_price = 0

if season == "Summer":
    destination = "Alaska"
elif season == "Winter":
    destination = "Morocco"

if budget <= 1000:
    stay_type = "Camp"
    if destination == "Alaska":
        vacation_price = budget * 0.65
    elif destination == "Morocco":
        vacation_price = budget * 0.45
elif 1000 < budget <= 3000:
    stay_type = "Hut"
    if destination == "Alaska":
        vacation_price = budget * 0.80
    elif destination == "Morocco":
        vacation_price = budget * 0.60
else:
    stay_type = "Hotel"
    vacation_price = budget * 0.90

print(f"{destination} - {stay_type} - {vacation_price:.2f}")
