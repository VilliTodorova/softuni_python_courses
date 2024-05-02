initial_string = input().split()
result = ''

for word in initial_string:
    result += word * len(word)

print(result)
