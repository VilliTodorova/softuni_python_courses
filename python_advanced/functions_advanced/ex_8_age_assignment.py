def age_assignment(*names, **person_info):
    result = []

    for letter, age in person_info.items():
        for name in names:
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")

    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
