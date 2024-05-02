season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())
price_per_night = 0
activity_type = ""
discount = 1

if season == "Winter":
    if group_type == "girls":
        price_per_night = 9.60
        activity_type = "Gymnastics"
    elif group_type == "boys":
        price_per_night = 9.60
        activity_type = "Judo"
    elif group_type == "mixed":
        price_per_night = 10.00
        activity_type = "Ski"
elif season == "Spring":
    if group_type == "girls":
        price_per_night = 7.20
        activity_type = "Athletics"
    elif group_type == "boys":
        price_per_night = 7.20
        activity_type = "Tennis"
    elif group_type == "mixed":
        price_per_night = 9.50
        activity_type = "Cycling"
elif season == "Summer":
    if group_type == "girls":
        price_per_night = 15.00
        activity_type = "Volleyball"
    elif group_type == "boys":
        price_per_night = 15.00
        activity_type = "Football"
    elif group_type == "mixed":
        price_per_night = 20.00
        activity_type = "Swimming"

if students_count >= 50:
    discount = 0.5
elif students_count >= 20:
    discount = 0.85
elif students_count >= 10:
    discount = 0.95
else:
    pass

total_price = nights_count * students_count * price_per_night * discount

print(f"{activity_type} {total_price:.2f} lv.")

