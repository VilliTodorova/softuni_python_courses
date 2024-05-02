numbers = []

for _ in range(int(input())):
    numbers_actions = input().split()
    action = numbers_actions[0]
    if action == "1":
        numbers.append(numbers_actions[1])
    elif action == "2":
        if numbers:
            numbers.pop()
    elif action == "3":
        if numbers:
            print(max(numbers))
    elif action == "4":
        if numbers:
            print(min(numbers))

numbers.reverse()
print(*numbers, sep=", ")
