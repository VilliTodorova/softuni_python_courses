finish = int(input())
start = int(input())
special = int(input())

for address in range(start, finish - 1, -1):
    if address % 2 == 0 and address % 3 == 0:
        if address == special:
            break
        print(f"{address}", end=" ")

