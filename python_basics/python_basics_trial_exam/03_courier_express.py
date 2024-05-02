package_weight = float(input())
service_type = input()  # "standard" или "express"
distance_km = int(input())
price_for_service = 0
added_cost_express = 0

if package_weight < 1:
    price_for_service = 0.03
elif 1 <= package_weight < 10:
    price_for_service = 0.05
elif 10 <= package_weight < 40:
    price_for_service = 0.10
elif 40 <= package_weight < 90:
    price_for_service = 0.15
elif 90 <= package_weight < 150:
    price_for_service = 0.20
if service_type == "express":
    if package_weight < 1:
        added_cost_express = price_for_service * 0.8
    elif 1 <= package_weight < 10:
        added_cost_express = price_for_service * 0.4
    elif 10 <= package_weight < 40:
        added_cost_express = price_for_service * 0.05
    elif 40 <= package_weight < 90:
        added_cost_express = price_for_service * 0.02
    elif 90 <= package_weight < 150:
        added_cost_express = price_for_service * 0.01

total_price = distance_km * price_for_service + distance_km * added_cost_express * package_weight

print(f"The delivery of your shipment with weight of {package_weight :.3f} kg. would cost {total_price :.2f} lv.")
