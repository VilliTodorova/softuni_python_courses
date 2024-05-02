factor = int(input())
count = int(input())
multiples = []

for i in range(1, count + 1):
    current_num = i * factor
    multiples.append(current_num)

print(sorted(multiples))
