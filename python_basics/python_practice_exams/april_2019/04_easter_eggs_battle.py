player_one_eggs = int(input())
player_two_eggs = int(input())
command = input()   # "one", "two" OR "End"
player_one_is_winner = True

while command != "End":
    if command == "one":
        player_two_eggs -= 1
    elif command == "two":
        player_one_eggs -= 1
    if player_one_eggs <= 0:
        player_one_is_winner = False
        break
    if player_two_eggs <= 0:
        break

    command = input()

if command == "End":
    print(f"Player one has {player_one_eggs} eggs left.\n"
          f"Player two has {player_two_eggs} eggs left.")
elif not player_one_is_winner:
    print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
else:
    print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
