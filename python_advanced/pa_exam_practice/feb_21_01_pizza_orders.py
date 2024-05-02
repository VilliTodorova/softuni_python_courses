from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
employee_cap = [int(x) for x in input().split(", ")]

total_count = 0

while pizza_orders and employee_cap:
    current_order = pizza_orders[0]
    current_employee = employee_cap[-1]

    if current_order <= 0:
        pizza_orders.popleft()
        continue
    elif current_order > 10:
        pizza_orders.popleft()
        continue

    if current_order <= current_employee:
        total_count += current_order
        pizza_orders.popleft()
        employee_cap.pop()
    else:
        total_count += current_employee
        pizza_orders[0] -= current_employee
        employee_cap.pop()
        continue

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_count}")
    print(f"Employees: {', '.join(map(str, employee_cap))}")

if not employee_cap:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")
