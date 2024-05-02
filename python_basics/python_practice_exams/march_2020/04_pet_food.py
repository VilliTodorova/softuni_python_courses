reference_days = int(input())
total_food = float(input())
day = 0
dog_eaten = 0
cat_eaten = 0
total_eaten = 0
total_biscuits = 0

for _ in range(reference_days):
    dog_current = int(input())
    cat_current = int(input())
    day += 1
    current_day_eaten = dog_current + cat_current
    if day % 3 == 0:
        biscuits_eaten = current_day_eaten * 0.1
        total_biscuits += biscuits_eaten
    else:
        pass
    dog_eaten += dog_current
    cat_eaten += cat_current
    total_eaten += current_day_eaten

percentage_eaten = total_eaten / total_food * 100
percentage_dog = dog_eaten / total_eaten * 100
percentage_cat = cat_eaten / total_eaten * 100
print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percentage_eaten :.2f}% of the food has been eaten.")
print(f"{percentage_dog :.2f}% eaten from the dog.")
print(f"{percentage_cat :.2f}% eaten from the cat.")
