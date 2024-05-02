items_to_buy = input().split("|")
budget = float(input())

CLOTHES_MAX = 50.00
SHOES_MAX = 35.00
ACCESSORIES_MAX = 20.50

sales = []
money_spent = 0

for item in items_to_buy:
    values = item.split("->")
    item_name = values[0]
    item_buy_price = float(values[1])
    sell_price = 0
    if item_name == "Clothes":
        if item_buy_price <= CLOTHES_MAX and item_buy_price <= budget:
            budget -= item_buy_price
            money_spent += item_buy_price
            sell_price = item_buy_price * 1.4
            sales.append(sell_price)

    elif item_name == "Shoes":
        if item_buy_price <= SHOES_MAX and item_buy_price <= budget:
            budget -= item_buy_price
            money_spent += item_buy_price
            sell_price = item_buy_price * 1.4
            sales.append(sell_price)
    elif item_name == "Accessories":
        if item_buy_price <= ACCESSORIES_MAX and item_buy_price <= budget:
            budget -= item_buy_price
            money_spent += item_buy_price
            sell_price = item_buy_price * 1.4
            sales.append(sell_price)

sales_float = list(map(float, sales))

for value in sales_float:
    print(f'{value:.2f}', end=" ")
print()
profit = (sum(sales_float)) - money_spent
print(f"Profit: {profit:.2f}")

if (sum(sales_float) + budget) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
