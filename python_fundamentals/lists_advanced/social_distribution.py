population = [int(number) for number in input().split(', ')]
min_wealth = int(input())
max_num = max(population)
for num in population:
    if num < min_wealth:
        difference = min_wealth - num
        population.remove(max_num)
        max_num -= difference
        population.append(max_num)
        num = min_wealth
        population.append(num)
    else:
        continue

for i in population:
    if i < min_wealth:
        population.remove(i)
print(sorted(population))
