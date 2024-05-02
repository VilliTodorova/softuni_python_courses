number_1 = int(input())
number_2 = int(input())
math_operator = input()  # "+", "-", "*", "/", "%"
result = 0

if math_operator == "+":
    result = number_1 + number_2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number_1} {math_operator} {number_2} = {result} - {even_or_odd}")
elif math_operator == "-":
    result = number_1 - number_2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number_1} {math_operator} {number_2} = {result} - {even_or_odd}")
elif math_operator == "*":
    result = number_1 * number_2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number_1} {math_operator} {number_2} = {result} - {even_or_odd}")
elif math_operator == "/":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        result = number_1 / number_2
        print(f"{number_1} {math_operator} {number_2} = {result:.2f}")
elif math_operator == "%":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        result = number_1 % number_2
        print(f"{number_1} {math_operator} {number_2} = {result}")
