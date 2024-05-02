def check_chairs(rooms):
    total_chairs = 0
    for current_room in range(1, rooms + 1):
        empty_chairs, visitors = input().split()
        current_chairs = len(empty_chairs) - int(visitors)
        total_chairs += current_chairs
        if current_chairs < 0:
            print(f"{abs(current_chairs)} more chairs needed in room {current_room}")

    return total_chairs


rooms = int(input())
total_free_chairs = check_chairs(rooms)

if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')
