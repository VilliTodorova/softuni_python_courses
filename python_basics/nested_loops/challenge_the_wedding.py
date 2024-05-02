men_count = int(input())
women_count = int(input())
max_tables = int(input())

for man in range(1, men_count + 1):
    for woman in range(1, women_count + 1):
        max_tables -= 1
        if max_tables < 0:
            break
        print(f"({man} <-> {woman})", end=" ")
