budget = float(input())
season = input()

stay = ""
destination = ""
price = 0

if budget <= 100 and season == "summer":
    destination = "Bulgaria"
    stay = "Camp"
    price = 0.3
elif budget <= 100 and season == "winter":
    destination = "Bulgaria"
    stay = "Hotel"
    price = 0.7
elif budget <= 1000 and season == "summer":
    destination = "Balkans"
    stay = "Camp"
    price = 0.4
elif budget <= 1000 and season == "winter":
    destination = "Balkans"
    stay = "Hotel"
    price = 0.8
elif budget >= 1000:
    destination = "Europe"
    stay = "Hotel"
    price = 0.9

total = price * budget

print(f"Somewhere in {destination}\n{stay} - {total:.2f}")
