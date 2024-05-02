food_in_grams = float(input()) * 1000
hay_in_grams = float(input()) * 1000
cover_in_grams = float(input()) * 1000
puppys_weight_in_grams = float(input()) * 1000
day = 1

while True:

    food_in_grams -= 300
    if day % 2 == 0:
        hay_in_grams -= food_in_grams * 0.05
    if day % 3 == 0:
        cover_in_grams -= puppys_weight_in_grams / 3

    if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0:
        print("Merry must go to the pet store!")
        break

    if day == 30:
        print(f"Everything is fine! Puppy is happy! Food: {(food_in_grams / 1000):.2f}, "
              f"Hay: {(hay_in_grams / 1000):.2f}, "
              f"Cover: {(cover_in_grams / 1000):.2f}.")
        break

    day += 1
