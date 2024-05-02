your_number = int(input())
counter_is_bigger = False
counter = 1

for row in range(1, your_number + 1):
    for column in range(1, row + 1):
        if counter > your_number:
            counter_is_bigger = True
            break
        print(str(counter) + " ", end="")
        counter += 1
    if counter_is_bigger:
        break
    print()
