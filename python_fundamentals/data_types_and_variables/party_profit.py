group_size = int(input())
adventure_days = int(input())
total_coins = 0

for day in range(1, adventure_days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    if day % 3 == 0:
        total_coins -= 3 * group_size
    if day % 5 == 0:
        total_coins += 20 * group_size
        if day % 3 == 0:
            total_coins -= 2 * group_size
    total_coins += 50
    total_coins -= 2 * group_size

coins_each = total_coins // group_size

print(f"{group_size} companions received {coins_each} coins each.")
