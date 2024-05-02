daily_pocket_money = float(input())
daily_earned_sales = float(input())
total_expenses = float(input())
gift_price = float(input())

total_profit = daily_pocket_money * 5 + daily_earned_sales * 5 - total_expenses

if total_profit >= gift_price:
    print(f"Profit: {total_profit :.2f} BGN, the gift has been purchased.")
else:
    insufficient = gift_price - total_profit
    print(f"Insufficient money: {insufficient :.2f} BGN.")
