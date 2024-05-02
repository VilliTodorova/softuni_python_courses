distance_to_pokemon = [int(number) for number in input().split()]
total_score = 0

while True:
    if len(distance_to_pokemon) <= 0:
        break

    index = int(input())
    score = 0
    if index < 0:
        score += distance_to_pokemon[0]
        for current_index in range(0, len(distance_to_pokemon)):
            if distance_to_pokemon[current_index] <= score:
                distance_to_pokemon[current_index] += score
            else:
                distance_to_pokemon[current_index] -= score
            distance_to_pokemon.pop(0)
            distance_to_pokemon.insert(0, distance_to_pokemon[-1])
    elif index > len(distance_to_pokemon) - 1:
        score += distance_to_pokemon[-1]
        for current_index in range(0, len(distance_to_pokemon)):
            if distance_to_pokemon[current_index] <= score:
                distance_to_pokemon[current_index] += score
            else:
                distance_to_pokemon[current_index] -= score
        distance_to_pokemon.pop()
        distance_to_pokemon.insert(distance_to_pokemon[-1], distance_to_pokemon[0])
    if index in range(0, len(distance_to_pokemon)):
        score += distance_to_pokemon[index]
        for current_index in range(0, len(distance_to_pokemon)):
            if distance_to_pokemon[current_index] <= score:
                distance_to_pokemon[current_index] += score
            else:
                distance_to_pokemon[current_index] -= score
        distance_to_pokemon.pop(index)
    total_score += score
print(total_score)

