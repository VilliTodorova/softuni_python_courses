actor_name = input()
actor_points = float(input())
jury_count = int(input())
character_count = 0
jury_points = 0

for jury in range(jury_count):
    jury_name = input()
    jury_points = float(input())
    character_count = len(jury_name)

    actor_points += (character_count * jury_points / 2)
    if actor_points >= 1250.5:
        break
needed_points = 1250.5 - actor_points

if actor_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
