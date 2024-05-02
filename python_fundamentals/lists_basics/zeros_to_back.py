initial = input().split(", ")

for i in initial:
    if i == "0":
        initial.remove(i)
        initial.append(i)

list_as_int = list(map(int, initial))
print(list_as_int)
