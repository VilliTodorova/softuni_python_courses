initial_string = input().split()
inverted_nums = []
for current_num in initial_string:
    num_as_inverted_int = -int(current_num)
    inverted_nums.append(num_as_inverted_int)

print(inverted_nums)
