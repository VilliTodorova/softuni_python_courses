from collections import deque

textiles = deque(int(x) for x in input().split())
meds = deque(int(x) for x in input().split())

healing_items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100,
}

crafted_elements = {}


def create_healing_items(textiles, meds):
    while textiles and meds:
        current_textile = textiles.popleft()
        current_med = meds.pop()
        current_sum = current_textile + current_med

        if current_sum in healing_items.values():
            for item, value in healing_items.items():
                if value == current_sum:
                    if item not in crafted_elements:
                        crafted_elements[item] = 0
                    crafted_elements[item] += 1

        elif current_sum > healing_items["MedKit"]:
            if "MedKit" not in crafted_elements:
                crafted_elements["MedKit"] = 0
            crafted_elements["MedKit"] += 1
            new_med = meds.pop()
            meds.append(current_med + current_textile - healing_items["MedKit"] + new_med)

        else:
            current_med += 10
            meds.append(current_med)


create_healing_items(textiles, meds)

result = [f"{key} - {value}" for key, value in sorted(crafted_elements.items(), key=lambda x: (-x[1], x[0]))]

if not textiles and not meds:
    print("Textiles and medicaments are both empty.")
    for item in result:
        print(item)
elif not textiles:
    print("Textiles are empty.")
    for item in result:
        print(item)
    meds.reverse()
    print(f"Medicaments left: {', '.join(map(str, meds))}")
else:
    print("Medicaments are empty.")
    for item in result:
        print(item)
    print(f"Textiles left: {', '.join(map(str, textiles))}")
