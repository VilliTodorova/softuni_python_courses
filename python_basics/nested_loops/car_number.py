start = int(input())
finish = int(input())
is_special = True
for a in range(start, finish + 1):
    for b in range(start, finish + 1):
        for c in range(start, finish + 1):
            for d in range(start, finish + 1):
                if ((a % 2 == 0 and d % 2 != 0) or (a % 2 != 0 and d % 2 == 0)) \
                        and a > d and (b + c) % 2 == 0:
                    print(f"{a}{b}{c}{d}", end=" ")
