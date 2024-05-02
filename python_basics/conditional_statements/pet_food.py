from math import floor, ceil

days_absent = int(input())
total_food_provided = int(input())
dog_food_day = float(input())
cat_food_day = float(input())
turtle_food_day = float(input()) / 1000

dog_needs = days_absent * dog_food_day
cat_needs = days_absent * cat_food_day
turtle_needs = days_absent * turtle_food_day
total_needed = dog_needs + cat_needs + turtle_needs
leftover_food = total_food_provided - total_needed

if total_food_provided > total_needed:
    print(f'{floor(leftover_food)} kilos of food left.')
else:
    print(f'{ceil(abs(leftover_food))} more kilos of food are needed.')
