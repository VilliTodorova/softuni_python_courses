from collections import deque

monster_armor = deque([int(x) for x in input().split(",")])
strike_impact = [int(x) for x in input().split(",")]

killed_monsters = 0

while monster_armor and strike_impact:

    soldier_power = strike_impact.pop()
    current_monster = monster_armor.popleft()

    if soldier_power >= current_monster:
        killed_monsters += 1
        soldier_power -= current_monster

        if strike_impact:
            strike_impact[-1] += soldier_power
        elif not strike_impact and soldier_power > 0:
            strike_impact.append(soldier_power)

    else:
        current_monster -= soldier_power
        monster_armor.append(current_monster)

if not strike_impact:
    print("The soldier has been defeated.")
if not monster_armor:
    print("All monsters have been killed!")

print(f"Total monsters killed: {killed_monsters}")
