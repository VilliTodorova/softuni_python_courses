joinery_count = int(input())
type_joinery = input()  # "90X130" OR "100X150" OR "130X180" OR "200X300"
delivery_info = input()  # "With delivery" OR "Without delivery"
single_price = 0
discount = 1
extra_discount = 1  # for count over 99

if joinery_count < 10:
    print("Invalid order")

if type_joinery == "90X130":
    single_price = 110
    if 30 <= joinery_count <= 60:
        discount = 0.95
    elif joinery_count > 60:
        discount = 0.92
elif type_joinery == "100X150":
    single_price = 140
    if 40 <= joinery_count <= 80:
        discount = 0.94
    elif joinery_count > 80:
        discount = 0.90
elif type_joinery == "130X180":
    single_price = 190
    if 20 <= joinery_count <= 50:
        discount = 0.93
    elif joinery_count > 50:
        discount = 0.88
elif type_joinery == "200X300":
    single_price = 250
    if 25 <= joinery_count <= 50:
        discount = 0.91
    elif joinery_count > 50:
        discount = 0.86

if joinery_count > 99:
    extra_discount = 0.96

price_without_extra = single_price * joinery_count * discount

if delivery_info == "With delivery":
    price_without_extra += 60
elif delivery_info == "Without delivery":
    pass

final_price = price_without_extra * extra_discount
if not joinery_count < 10:
    print(f"{final_price :.2f} BGN")
