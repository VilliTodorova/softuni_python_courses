minutes_walking_daily = int(input())
daily_walks_count = int(input())
daily_calories_intake = int(input())

calories_burned = minutes_walking_daily * 5 * daily_walks_count

if calories_burned >= (daily_calories_intake * 0.5):

    # •	Ако изгорените калории през разходката са повече или равни на  50% от приетите през деня калории:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
# •	Ако  изгорените калории през разходката са по-малко от 50% от приетите през деня калории:
else:

    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
