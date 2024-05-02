snowballs_count = int(input())
max_value = 0
max_weight = 0
max_time = 0
max_quality = 0

for ball in range(snowballs_count):
    snowball_weight = int(input())
    time_to_target = int(input())
    quality = int(input())
    snowball_value = (snowball_weight / time_to_target) ** quality
    if snowball_value > max_value:
        max_value = snowball_value
        max_weight = snowball_weight
        max_time = time_to_target
        max_quality = quality

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")

