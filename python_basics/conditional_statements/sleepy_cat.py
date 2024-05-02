from math import floor

days_off = int(input())
at_work_playtime = 63
at_off_playtime = 127
yearly_norm = 30000

total_work_playtime = (365 - days_off) * at_work_playtime
total_off_playtime = days_off * at_off_playtime
leftover_time = abs(yearly_norm - (total_off_playtime + total_work_playtime))
leftover_time_hours = (floor(leftover_time // 60))
leftover_time_minutes = (leftover_time % 60)
# print(leftover_time_hours)
# print(leftover_time_minutes)

if total_work_playtime + total_off_playtime > yearly_norm:
    print(f'Tom will run away\n{leftover_time_hours} hours '
          f'and {leftover_time_minutes} minutes more for play')
else:
    print(f'Tom sleeps well\n{leftover_time_hours} '
          f'hours and {leftover_time_minutes} minutes less for play')
