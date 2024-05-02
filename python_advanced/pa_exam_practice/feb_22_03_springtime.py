def start_spring(**spring_objects):
    new_dict = {}

    for k, v in spring_objects.items():
        if v not in new_dict:
            new_dict[v] = [k]
        if k not in new_dict[v]:
            new_dict[v].append(k)

    sorted_result = {k: sorted(v) for k, v in sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0]))}

    result = ""
    for key, value in sorted_result.items():
        result += f"{key}:\n"
        for val in value:
            result += f"-{val}\n"

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",
                   }

print(start_spring(**example_objects))
