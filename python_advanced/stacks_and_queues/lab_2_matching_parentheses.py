expression = input()
parentheses_index = []

for index in range(0, len(expression)):
    if expression[index] == "(":
        parentheses_index.append(index)
    elif expression[index] == ")":
        start_index = parentheses_index.pop()
        end_index = index + 1
        print(expression[start_index:end_index])