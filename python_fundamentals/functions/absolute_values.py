initial_numbers = input().split()
initial_numbers = [float(number) for number in initial_numbers]
absolutes = list(map(abs, initial_numbers))
print(absolutes)
