food_bought_kg = int(input())
food_bought_grams = food_bought_kg * 1000
total_eaten = 0
leftover = 0
insufficient = 0
command = input()
is_enough = True

while command != "Adopted":
    food_eaten_per_day = int(command)
    total_eaten += food_eaten_per_day
    if total_eaten > food_bought_grams:
        is_enough = False
        insufficient = total_eaten - food_bought_grams
    else:
        leftover = food_bought_grams - total_eaten

    if command == "Adopted":
        break
    command = input()
if is_enough:
    print(f"Food is enough! Leftovers: {leftover} grams.")
else:
    print(f"Food is not enough. You need {insufficient} grams more.")