your_text = input()

new_text = [char for char in your_text if char.lower() not in ['a', 'o', 'u', 'e', 'i']]
result = "".join(new_text)
print(result)