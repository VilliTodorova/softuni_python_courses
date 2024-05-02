from collections import deque

caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque(int(x) for x in input().split(", "))
intake = 0

while True:
    if not caffeine:
        break
    if not energy_drinks:
        break

    current_caffeine = caffeine.pop()
    current_drink = energy_drinks.popleft()
    drink_caff_amount = current_caffeine * current_drink

    if intake + drink_caff_amount <= 300:
        intake += drink_caff_amount
    else:
        energy_drinks.append(current_drink)
        if (intake - 30) >= 0:
            intake -= 30
        else:
            intake = 0

if not energy_drinks:
    print("At least Stamat wasn'project exceeding the maximum caffeine.")
else:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")

print(f"Stamat is going to sleep with {intake} mg caffeine.")
