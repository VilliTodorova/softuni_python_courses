from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

crafted_presents = []


def is_done(crafted_presents):
    return ("Doll" in crafted_presents and "Train" in crafted_presents) or \
           ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents)


possible_presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_levels:
    current_material = materials.pop() if magic_levels[0] or not materials[-1] else 0
    current_magic = magic_levels.popleft() if current_material or not magic_levels[0] else 0

    product = current_material * current_magic

    if possible_presents.get(product):
        crafted_presents.append(possible_presents[product])
    elif product < 0:
        materials.append(current_material + current_magic)
    elif product > 0:
        materials.append(current_material + 15)

    if current_magic == 0:
        pass
    if current_material == 0:
        pass

if is_done(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    materials.reverse()
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join([str(i) for i in magic_levels])}")

for gift in sorted(set(crafted_presents)):
    print(f"{gift}: {crafted_presents.count(gift)}")
