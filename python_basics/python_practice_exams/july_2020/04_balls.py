from math import floor

balls_quantity = int(input())
points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_balls = 0

for ball in range(balls_quantity):
    color_picked = input()
    if color_picked == "red":
        points += 5
        red_balls += 1
    elif color_picked == "orange":
        points += 10
        orange_balls += 1
    elif color_picked == "yellow":
        points += 15
        yellow_balls += 1
    elif color_picked == "white":
        points += 20
        white_balls += 1
    elif color_picked == "black":
        points = floor(points / 2)
        black_balls += 1
    else:
        other_balls += 1

print(f"Total points: {points}\n"
      f"Red balls: {red_balls}\n"
      f"Orange balls: {orange_balls}\n"
      f"Yellow balls: {yellow_balls}\n"
      f"White balls: {white_balls}\n"
      f"Other colors picked: {other_balls}\n"
      f"Divides from black balls: {black_balls}")
