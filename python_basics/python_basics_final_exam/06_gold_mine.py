locations_count = int(input())

for location in range(locations_count):
    average_expected = float(input())
    days_mining = int(input())
    total_mined = 0
    for day in range(days_mining):
        gold_mined = float(input())
        total_mined += gold_mined
    average_per_day = total_mined / days_mining

    if average_per_day >= average_expected:
        print(f"Good job! Average gold per day: {average_per_day :.2f}.")
    elif average_per_day < average_expected:
        difference = average_expected - average_per_day
        print(f"You need {difference :.2f} gold.")
