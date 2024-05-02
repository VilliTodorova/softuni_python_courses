budget = int(input())
in_overdraft = False
command = input()

while command != "End":
    price = int(command)
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        in_overdraft = True
        break

    command = input()

if not in_overdraft:
    print("You bought everything needed.")
