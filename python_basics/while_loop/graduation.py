student_name = input()
current_grade = 1
total_score = 0
failed_attempts = 0

while current_grade <= 12:
    current_score = float(input())
    if current_score < 4:
        failed_attempts += 1
        if failed_attempts > 1:
            break
        continue
    current_grade += 1
    total_score += current_score

average_score = total_score / 12

if current_grade == 13:
    print(f"{student_name} graduated. Average grade: {average_score:.2f}")
else:
    print(f"{student_name} has been excluded at {current_grade} grade")
