lines_count = int(input())

max_intersect = set()

for diapason in range(lines_count):
    first_range, second_range = [data.split(",") for data in input().split("-")]

    first_set = set(range(int(first_range[0]), int(first_range[1]) + 1))
    second_set = set(range(int(second_range[0]), int(second_range[1]) + 1))

    intersection = list(first_set.intersection(second_set))

    if len(intersection) > len(max_intersect):
        max_intersect = intersection

print(f"Longest intersection is {max_intersect} with length {len(max_intersect)}")
