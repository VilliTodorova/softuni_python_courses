def accommodate_new_pets(hotel_capacity: int, max_weight: float, *animal_data):

    pets_dict = {}
    result = []

    for current_animal, current_weight in animal_data:

        if hotel_capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break

        if current_weight > max_weight:
            continue

        if current_animal not in pets_dict:
            pets_dict[current_animal] = 0

        pets_dict[current_animal] += 1
        hotel_capacity -= 1

    else:
        result.append(f"All pets are accommodated! Available capacity: {hotel_capacity}.")

    result.append("Accommodated pets:")

    [result.append(f"{key}: {value}") for key, value in sorted(pets_dict.items())]

    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
