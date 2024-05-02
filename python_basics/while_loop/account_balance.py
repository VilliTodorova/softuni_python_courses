command = input()
account_balance = 0

while command != "NoMoreMoney":
    current_sum = float(command)

    if current_sum < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {current_sum:.2f}")
    account_balance += current_sum
    command = input()

print(f"Total: {account_balance:.2f}")
