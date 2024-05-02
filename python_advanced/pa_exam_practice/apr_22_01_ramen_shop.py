from collections import deque

bowls_ramen = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))

while bowls_ramen and customers:

    current_ramen = bowls_ramen.pop()
    current_customer = customers.popleft()

    if current_ramen == current_customer:
        continue

    elif current_ramen > current_customer:
        current_ramen -= current_customer
        bowls_ramen.append(current_ramen)
        continue

    elif current_ramen < current_customer:
        current_customer -= current_ramen
        customers.appendleft(current_customer)
        continue

if not customers:
    print("Great job! You served all the customers.")
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls_ramen))}")
else:
    print("Out of ramen! You didn'project manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")
