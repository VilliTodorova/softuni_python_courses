names = input().split(', ')

sorted_names_alpha = sorted(names, key=lambda x: (-len(x), x))

print(sorted_names_alpha)
