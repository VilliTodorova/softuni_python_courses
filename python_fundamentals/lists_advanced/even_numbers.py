def find_even_indices(nums_list):
    even_indices = [index for index, element in enumerate(nums_list) if element % 2 == 0]
    return even_indices


nums_list = list(map(int, input().split(', ')))
result = find_even_indices(nums_list)

print(result)
