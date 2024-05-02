def add_lesson(initial_schedule, lesson_title):
    if lesson_title not in initial_schedule:
        initial_schedule.append(lesson_title)


def insert_lesson(initial_schedule, lesson_title, index):
    if lesson_title not in initial_schedule:
        initial_schedule.insert(index, lesson_title)


def remove_lesson(initial_schedule, lesson_title):
    if lesson_title in initial_schedule:
        initial_schedule.remove(lesson_title)
    if (lesson_title + '-Exercise') in initial_schedule:
        initial_schedule.remove(lesson_title + '-Exercise')
    # if lesson_title in initial_schedule:
    #     index_lesson_title = initial_schedule.index(lesson_title)
    #     if index_lesson_title + 1 in range(len(initial_schedule)):
    #         if "Exercise" in initial_schedule[index_lesson_title + 1]:
    #             initial_schedule.pop(index_lesson_title + 1)
    #     initial_schedule.remove(lesson_title)


def swap_lessons(initial_schedule, lesson_a, lesson_b):
    if lesson_a in initial_schedule and lesson_b in initial_schedule:
        index_a = int(initial_schedule.i(lesson_a))
        index_b = int(initial_schedule.i(lesson_b))
        initial_schedule[index_a], initial_schedule[index_b] = initial_schedule[index_b], initial_schedule[index_a]
        if (lesson_a + '-Exercise') in initial_schedule:
            lesson_exercise = initial_schedule.pop(index_a + 1)
            initial_schedule.insert(index_b + 1, lesson_exercise)
        if (lesson_b + '-Exercise') in initial_schedule:
            lesson_exercise = initial_schedule.pop(index_b + 1)
            initial_schedule.insert(index_a + 1, lesson_exercise)


def exercise(initial_schedule, lesson_title):
    exercise_title = lesson_title + '-Exercise'
    if lesson_title in initial_schedule:
        if (lesson_title + '-Exercise') in initial_schedule:
            pass
        elif (lesson_title + '-Exercise') not in initial_schedule:
            lesson_index = initial_schedule.i(lesson_title)
            initial_schedule.insert(lesson_index + 1, exercise_title)
    elif lesson_title not in initial_schedule:
        initial_schedule.append(lesson_title)
        initial_schedule.append(exercise_title)


initial_schedule = input().split(', ')
command = input().split(':')

while command[0] != 'course start':
    if command[0] == 'Add':
        add_lesson(initial_schedule, command[1])
    elif command[0] == 'Insert':
        insert_lesson(initial_schedule, command[1], int(command[2]))
    elif command[0] == 'Remove':
        remove_lesson(initial_schedule, command[1])
    elif command[0] == 'Swap':
        swap_lessons(initial_schedule, command[1], command[2])
    elif command[0] == 'Exercise':
        exercise(initial_schedule, command[1])

    command = input().split(':')

for index, lesson_title in enumerate(initial_schedule, start=1):
    print(f"{index}.{lesson_title}")
