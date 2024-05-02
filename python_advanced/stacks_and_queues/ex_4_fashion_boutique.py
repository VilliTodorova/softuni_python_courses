boxed_clothes = list(int(x) for x in input().split())
rack_capacity = int(input())
racks_count = 1
current_space = rack_capacity

while boxed_clothes:
    clothes = boxed_clothes.pop()
    if current_space >= clothes:
        current_space -= clothes
    else:
        racks_count += 1
        current_space = rack_capacity - clothes

print(racks_count)
