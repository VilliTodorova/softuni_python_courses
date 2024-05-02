import math


def cartesian_distance_center(x, y):
    # Calculate the distance from a given point to the center of the coordinate system
    distance_to_center = math.sqrt(x ** 2 + y ** 2)
    return distance_to_center


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))

# call the function to calculate distances by the given coordinates
distance1 = cartesian_distance_center(x1, y1)
distance2 = cartesian_distance_center(x2, y2)

# check which distance is closer and print the result
if distance1 <= distance2:
    print(f'({x1}, {y1})')
else:
    print(f'({x2}, {y2})')
