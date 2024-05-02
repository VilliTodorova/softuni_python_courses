command = input()
best_player_name = ""
max_goals = 0
hat_trick = False

while command != "END":
    player_name = command
    goals_scored = int(input())
    if goals_scored > max_goals:
        max_goals = goals_scored
        best_player_name = player_name
    if 3 <= goals_scored < 10:
        hat_trick = True
    elif goals_scored >= 10:
        hat_trick = True
        break
    command = input()

print(f"{best_player_name} is the best player!")
if hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
