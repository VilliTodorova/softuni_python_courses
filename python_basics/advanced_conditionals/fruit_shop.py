fruit = input()
day = input()
quantity = float(input())
price = 0

fruit_prices_weekday = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}
fruit_prices_weekend = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

if fruit in fruit_prices_weekday and day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    price = fruit_prices_weekday[fruit]
elif fruit in fruit_prices_weekend and day in ["Saturday", "Sunday"]:
    price = fruit_prices_weekend[fruit]

else:
    print("error")
    exit()

total = quantity * price
print(f"{total :.2f}")
