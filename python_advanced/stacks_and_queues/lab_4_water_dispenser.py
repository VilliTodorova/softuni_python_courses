from collections import deque

quantity_water = int(input())  # in liters
names = input()
wait_list = deque()

while names != "Start":
    wait_list.append(names)
    names = input()

command = input()

while command != "End":
    actions = command.split()
    if len(actions) == 1:
        liters_needed = int(actions[0])
        if (quantity_water - liters_needed) >= 0:
            quantity_water -= liters_needed
            print(f"{wait_list.popleft()} got water")
        else:
            print(f"{wait_list.popleft()} must wait")
    else:
        refill_quantity = int(actions[1])
        quantity_water += refill_quantity

    command = input()


print(f"{quantity_water} liters left")
