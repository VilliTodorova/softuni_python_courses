def is_palindrome(num):
    return num == num[::-1]


your_sequence = input().split(', ')
for entry in your_sequence:
    num = str(entry)
    if is_palindrome(num):
        print("True")
    else:
        print("False")
