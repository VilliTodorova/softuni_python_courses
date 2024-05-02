command = input().split(' : ')
course_attendance = {}

while command[0] != 'end':
    course_name, student = command[0], command[1]
    if course_name not in course_attendance:
        course_attendance[course_name] = [student]
    else:
        course_attendance[course_name].append(student)

    command = input().split(' : ')

for (key, value) in course_attendance.items():
    print(f"{key}: {len(value)}")
    for name in course_attendance[key]:
        print(f"-- {name}")
