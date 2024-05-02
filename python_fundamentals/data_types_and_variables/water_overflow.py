num_lines = int(input())
liters_filled = 0

for i in range(num_lines):
    current_fill = int(input())
    if liters_filled + current_fill <= 255:
        liters_filled += current_fill
    else:
        print("Insufficient capacity!")
        continue

print(liters_filled)
