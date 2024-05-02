age = float(input())
gender = input()

if gender == "f" and age >= 16:
    print("Ms.")
elif gender == "f" and age < 16:
    print("Miss")
elif gender == "m" and age >= 16:
    print("Mr.")
else:
    print("Master")

# age = float(input())
# gender = input()
#
# if gender == "f":
#     if age >= 16:
#         print("Ms.")
#     else:
#         print("Miss")
# else:
#     if age >= 16:
#         print("Mr.")
#     else:
#         print("Master")
