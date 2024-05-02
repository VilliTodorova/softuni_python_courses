sequence_cards = input().split()
new_sequence = []
terminated_game = False

for i in sequence_cards:
    if i not in new_sequence:
        new_sequence.append(i)

team_a = 11
team_b = 11

for card in new_sequence:
    if "A" in card:
        team_a -= 1
    elif "B" in card:
        team_b -= 1
    if (team_a < 7) or (team_b < 7):
        terminated_game = True
        break

print(f'Team A - {team_a}; Team B - {team_b}')
if terminated_game:
    print('Game was terminated')
