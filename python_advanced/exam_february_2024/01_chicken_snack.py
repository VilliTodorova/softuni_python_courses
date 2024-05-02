from collections import deque

money_available = [int(x) for x in input().split()]
food_prices = deque(int(x) for x in input().split())

food_eaten = 0

while money_available and food_prices:

    current_money = money_available.pop()
    current_price = food_prices.popleft()

    if current_money == current_price:
        food_eaten += 1
    elif current_money > current_price:
        food_eaten += 1
        change = current_money - current_price
        if money_available:
            money_available[-1] += change
        else:
            money_available.append(change)
    else:
        continue

if food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
elif food_eaten == 0:
    print("Henry remained hungry. He will try next weekend again.")
else:
    if food_eaten == 1:
        print(f"Henry ate: {food_eaten} food.")
    else:
        print(f"Henry ate: {food_eaten} foods.")