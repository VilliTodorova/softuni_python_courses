from math import floor

world_record_seconds = float(input())
distance_in_meters = float(input())
time_per_one_meter = float(input())

resistance = floor(distance_in_meters / 50) * 30

george_time = distance_in_meters * time_per_one_meter + resistance
leftover = george_time - world_record_seconds

if george_time < world_record_seconds:
    print(f"Yes! The new record is {george_time :.2f} seconds.")
else:
    print(f"No! He was {leftover :.2f} seconds slower.")
