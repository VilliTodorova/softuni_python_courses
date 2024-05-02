xp_needed = float(input())
battles_count = int(input())
current_battle = 1

while current_battle <= battles_count:
    current_xp_gained = float(input())

    if current_battle % 3 == 0:
        current_xp_gained *= 1.15
    if current_battle % 5 == 0:
        current_xp_gained *= 0.9
    if current_battle % 15 == 0:
        current_xp_gained *= 1.05

    xp_needed -= current_xp_gained

    if xp_needed <= 0:
        break

    current_battle += 1

if xp_needed > 0:
    print(f"Player was not able to collect the needed experience, {xp_needed:.2f} more needed.")
else:
    print(f"Player successfully collected his needed experience for {current_battle} battles.")
