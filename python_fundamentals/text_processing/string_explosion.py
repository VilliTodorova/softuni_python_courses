your_string = list(input())
explosion_impact = 0
result_string = ""


for index in range(len(your_string)):
    if explosion_impact > 0 and your_string[index] != ">":
        explosion_impact -= 1
    elif your_string[index] == '>':
        explosion_impact += int(your_string[index + 1])
        result_string += your_string[index]
    else:
        result_string += your_string[index]

print(result_string)
