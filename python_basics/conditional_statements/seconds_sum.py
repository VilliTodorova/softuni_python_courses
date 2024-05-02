import math

time_first = int(input())
time_second = int(input())
time_third = int(input())
total_time = time_first + time_second + time_third

minutes_base = (total_time // 60)
minutes = math.floor(minutes_base)
seconds = total_time % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
