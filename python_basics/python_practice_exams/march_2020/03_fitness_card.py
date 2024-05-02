budget = float(input())
gender = input()    # m OR f
age = int(input())  # if age <= 19, discount 20%
activity_type = input()  # Gym	Boxing	Yoga	Zumba	Dances	Pilates
gym_card_price = 0

if gender == "m":
    if activity_type == "Gym":
        gym_card_price = 42
    elif activity_type == "Boxing":
        gym_card_price = 41
    elif activity_type == "Yoga":
        gym_card_price = 45
    elif activity_type == "Zumba":
        gym_card_price = 34
    elif activity_type == "Dances":
        gym_card_price = 51
    elif activity_type == "Pilates":
        gym_card_price = 39
elif gender == "f":
    if activity_type == "Gym":
        gym_card_price = 35
    elif activity_type == "Boxing":
        gym_card_price = 37
    elif activity_type == "Yoga":
        gym_card_price = 42
    elif activity_type == "Zumba":
        gym_card_price = 31
    elif activity_type == "Dances":
        gym_card_price = 53
    elif activity_type == "Pilates":
        gym_card_price = 37

if age <= 19:
    gym_card_price *= 0.80
else:
    pass

needed_money = gym_card_price - budget
if budget >= gym_card_price:
    print(f"You purchased a 1 month pass for {activity_type}.")
else:
    print(f"You don't have enough money! You need ${needed_money :.2f} more.")
