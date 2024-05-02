exam_time_hour = int(input())
exam_time_minutes = int(input())
arrival_time_hour = int(input())
arrival_time_minutes = int(input())

exam_time_converted = exam_time_hour * 60 + exam_time_minutes
arrival_time_converted = arrival_time_hour * 60 + arrival_time_minutes

difference = arrival_time_converted - exam_time_converted

if difference > 0:
    print("Late")
    if difference < 60:
        print(f"{abs(difference)} minutes after the start")
    else:
        minutes = abs(difference) % 60
        hours = abs(difference) // 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif difference >= -30:
    print("On time")
    if difference != 0:
        print(f"{abs(difference)} minutes before the start")
else:
    print("Early")
    if difference > -60:
        print(f"{abs(difference)} minutes before the start")
    else:
        minutes = abs(difference) % 60
        hours = abs(difference) // 60
        print(f"{hours}:{minutes:02d} hours before the start")
