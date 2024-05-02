temperature = int(input())
time_of_day = input()
outfit = ""
shoes = ""

if 10 <= temperature <= 18 and time_of_day == "Morning":
    outfit = "Sweatshirt"
    shoes = "Sneakers"
elif 10 <= temperature <= 18 and time_of_day == "Afternoon":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 10 <= temperature <= 18 and time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 18 < temperature <= 24 and time_of_day == "Morning":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 18 < temperature <= 24 and time_of_day == "Afternoon":
    outfit = "T-Shirt"
    shoes = "Sandals"
elif 18 < temperature <= 24 and time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
elif temperature >= 25 and time_of_day == "Morning":
    outfit = "T-Shirt"
    shoes = "Sandals"
elif temperature >= 25 and time_of_day == "Afternoon":
    outfit = "Swim Suit"
    shoes = "Barefoot"
elif temperature >= 25 and time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
