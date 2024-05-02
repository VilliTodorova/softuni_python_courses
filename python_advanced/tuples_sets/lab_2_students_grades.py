students_count = int(input())

student_info = tuple([data for data in input().split()] for _ in range(students_count))

students_dict = {}
for student, grade in student_info:
    if student not in students_dict:
        students_dict[student] = [float(grade)]
    else:
        students_dict[student].append(float(grade))

for pupil, grades in students_dict.items():
    avg_grade = sum(grades) / len(grades)
    formatted_grades = [f"{g:.2f}" for g in grades]
    grades_str = ' '.join(formatted_grades)
    print(f"{pupil} -> {grades_str} (avg: {avg_grade:.2f})")
