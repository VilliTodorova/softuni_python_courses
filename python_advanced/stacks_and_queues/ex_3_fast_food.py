from collections import deque

food_quantity = int(input())

orders = deque(int(x) for x in input().split())

print(max(orders))

for order in orders.copy():
    if (food_quantity - order) >= 0:
        food_quantity -= order
        orders.popleft()
    else:
        break

if orders:
    print(f"Orders left: ", end="")
    print(*orders)
else:
    print("Orders complete")
