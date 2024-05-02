from collections import deque

chocolate = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and chocolate and cups_of_milk:
    last_choc = chocolate[-1]
    first_cup = cups_of_milk[0]

    if last_choc <= 0 and first_cup <= 0:
        chocolate.pop()
        cups_of_milk.popleft()
        continue
    if last_choc <= 0:
        chocolate.pop()
        continue
    if first_cup <= 0:
        cups_of_milk.popleft()
        continue

    if last_choc == first_cup:
        chocolate.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        cups_of_milk.popleft()
        cups_of_milk.append(first_cup)
        chocolate[-1] -= 5

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join([str(i) for i in chocolate]) if chocolate else 'empty'}")
print(f"Milk: {', '.join([str(i) for i in cups_of_milk]) if cups_of_milk else 'empty'}")
