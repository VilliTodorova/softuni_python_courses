def is_balanced(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != bracket_pairs[char]:
                return "NO"

    return "YES" if not stack else "NO"


sequence = input()
result = is_balanced(sequence)
print(result)
