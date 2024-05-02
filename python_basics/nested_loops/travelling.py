destination = input()

while destination != "End":
    minimal_budget = float(input())
    saved_money = 0
    while saved_money < minimal_budget:
        money_in = float(input())
        saved_money += money_in
    print(f"Going to {destination}!")
    destination = input()
