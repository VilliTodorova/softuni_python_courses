def students_credits(*course_data):
    all_courses = {}

    for i in range(len(course_data)):
        course_name, max_credits, max_points, diyans_points = course_data[i].split("-")

        current_ratio = int(diyans_points) / int(max_points)
        current_course_credits = int(max_credits) * current_ratio

        all_courses[course_name] = current_course_credits

    result = ""

    total_sum = sum(all_courses.values())
    if total_sum >= 240:
        result += f"Diyan gets a diploma with {total_sum:.1f} credits.\n"
    else:
        result += f"Diyan needs {(240 - total_sum):.1f} credits more for a diploma.\n"

    for course_name, current_course_credits in sorted(all_courses.items(), key=lambda x: x[1], reverse=True):
        result += f"{course_name} - {current_course_credits:.1f}\n"

    return result


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
