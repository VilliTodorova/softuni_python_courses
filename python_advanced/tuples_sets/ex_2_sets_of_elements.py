n, m = [int(x) for x in input().split()]

first_set = set(input() for _ in range(n))
second_set = set(input() for _ in range(m))

print("\n".join(first_set.intersection(second_set)))
