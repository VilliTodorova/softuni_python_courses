import math

current_world_record = float(input())
distance_meters = float(input())
time_per_meter = float(input())

needed_time = distance_meters * time_per_meter
resistance = math.floor(distance_meters / 15) * 12.5
ivans_time = needed_time + resistance

if ivans_time < current_world_record:
    print(f'Yes, he succeeded! The new world record is {ivans_time :.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(ivans_time - current_world_record) :.2f} seconds slower.')
