students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendance = 0

for student in range(1, students_count + 1):
    current_attendance_count = int(input())
    total_current_bonus = current_attendance_count / lectures_count * (5 + additional_bonus)
    if total_current_bonus > max_bonus:
        max_bonus = total_current_bonus
        max_attendance = current_attendance_count

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
