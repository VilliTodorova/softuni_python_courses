from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
process_symbols = deque(input().split())

total_honey = 0


calculate_nectar = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y if y != 0 else 0,
}


while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        total_honey += abs(calculate_nectar[process_symbols.popleft()](current_bee, current_nectar))
    else:
        working_bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(i) for i in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(i) for i in nectar])}")

