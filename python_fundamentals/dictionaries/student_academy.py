count_input = int(input())
student_scores = {}

for i in range(count_input):
    student_name = input()
    current_grade = float(input())
    if student_name not in student_scores:
        student_scores[student_name] = [current_grade]
    else:
        student_scores[student_name].append(current_grade)

for (key, value) in student_scores.items():
    average_score = sum(student_scores[key]) / len(value)
    if average_score >= 4.50:
        print(f"{key} -> {average_score:.2f}")
