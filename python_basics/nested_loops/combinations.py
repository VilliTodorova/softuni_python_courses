your_number = int(input())
counter = 0

for x in range(0, your_number + 1):
    for y in range(0, your_number + 1):
        for z in range(0, your_number + 1):
            if x + y + z == your_number:
                counter += 1

print(counter)
