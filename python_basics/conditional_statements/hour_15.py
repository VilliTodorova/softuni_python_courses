hours = int(input())
minutes = int(input())

if minutes < 45:
    minutes += 15
else:
    hours = (hours + 1) % 24
    minutes = (minutes + 15) % 60

# print("{:01d}:{:02d}".format(hours, minutes))
print(f'{hours:01d}:{minutes:02d}')
