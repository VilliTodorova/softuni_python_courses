import math

tournaments_count = int(input())
initial_points = int(input())
winner_stage = 0
tournament_points = 0

for tournament in range(tournaments_count):
    stage_reached = input()

    if stage_reached == "W":
        tournament_points += 2000
        winner_stage += 1
    elif stage_reached == "F":
        tournament_points += 1200
    elif stage_reached == "SF":
        tournament_points += 720

average_points = tournament_points / tournaments_count
winning_percentage = winner_stage / tournaments_count * 100
total_points = initial_points + tournament_points

print(f"Final points: {total_points}\n"
      f"Average points: {math.floor(average_points)}\n"
      f"{winning_percentage:.2f}%")
