money_needed = float(input())
saved_money = float(input())
days_past = 0
days_spending = 0

while saved_money < money_needed and days_spending < 5:
    action = input()
    current_money = float(input())
    days_past += 1
    if action == "save":
        saved_money += current_money
        days_spending = 0
    elif action == "spend":
        saved_money -= current_money
        days_spending += 1
        if saved_money < 0:
            saved_money = 0

if days_spending == 5:
    print(f"You can't save the money.\n"
          f"{days_past}")
if saved_money >= money_needed:
    print(f"You saved the money for {days_past} days.")
