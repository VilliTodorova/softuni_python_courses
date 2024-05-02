tournament_days = int(input())
raised_money = 0
daily_winner = 0

for _ in range(tournament_days):
    daily_raised = 0
    won_games = 0
    lost_games = 0
    command = input()
    while command != "Finish":
        games_name = command
        win_or_lose = input()
        if win_or_lose == "win":
            daily_raised += 20
            won_games += 1
        elif win_or_lose == "lose":
            lost_games += 1
        command = input()

    if won_games > lost_games:
        daily_raised *= 1.1
        daily_winner += 1
    raised_money += daily_raised

if daily_winner > tournament_days / 2:
    raised_money *= 1.2
    print(f"You won the tournament! Total raised money: {raised_money :.2f}")
else:
    print(f"You lost the tournament! Total raised money: {raised_money :.2f}")
