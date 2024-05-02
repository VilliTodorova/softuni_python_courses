food_bought_kg = int(input())
food_bought_grams = food_bought_kg * 1000
command = input()

while command != "Adopted":
    food_bought_grams -= int(command)
    command = input()

if food_bought_grams >= 0:
    print(f"Food is enough! Leftovers: {food_bought_grams} grams.")
else:
    print(f"Food is not enough. You need {abs(food_bought_grams)} grams more.")
