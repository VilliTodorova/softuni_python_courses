def gather_credits(needed_credits, *course_data):
    enrolled_courses = []
    total_credits = 0

    for course_name, course_credits in course_data:

        if total_credits >= needed_credits:
            break

        if course_name in enrolled_courses:
            continue

        enrolled_courses.append(course_name)
        total_credits += course_credits

    if total_credits < needed_credits:
        return f"You need to enroll in more courses! You have to gather {needed_credits - total_credits} credits more."
    else:
        return f"Enrollment finished! Maximum credits: {total_credits}.\n" \
               f"Courses: {', '.join(sorted(enrolled_courses))}"


print(gather_credits(
    80,
    ("Basics", 27),
))


