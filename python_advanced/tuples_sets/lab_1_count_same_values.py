sequence = input().split()

unique_nums = {}    # key - num; value - count

for num in sequence:
    if num not in unique_nums:
        unique_nums[num] = 1
    else:
        unique_nums[num] += 1

for key, value in unique_nums.items():
    key = float(key)
    print(f"{key:.1f} - {value} times")


# from collections import Counter
#
# sequence = input().split()
#
# unique_nums = Counter(sequence)    # key - num; value - count
#
# for key, value in unique_nums.items():
#     key = float(key)
#     print(f"{key:.1f} - {value} times")
