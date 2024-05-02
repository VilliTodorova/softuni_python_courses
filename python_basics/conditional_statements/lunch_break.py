from math import ceil

tv_show_name = input()
show_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration / 8
relax_duration = break_duration / 4

leftover_break = (break_duration - lunch_duration - relax_duration)
free_time = (leftover_break - show_duration)

if free_time >= 0:
    print(f"You have enough time to watch {tv_show_name} and left with {ceil(free_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_show_name}, you need {ceil(abs(free_time))} more minutes.")