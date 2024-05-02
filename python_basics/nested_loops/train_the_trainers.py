# need a program to calculate the average score on a presentation
# at the end it needs to calculate the average score on all presentations

jury_count = int(input())
command = input()
total_score = 0
presentation_count = 0

while command != "Finish":
    presentation_name = command
    presentation_score = 0
    jury_score = 0

    for jury in range(jury_count):
        jury_score = float(input())
        presentation_score += jury_score

    average_on_presentation = presentation_score / jury_count

    print(f"{presentation_name} - {average_on_presentation :.2f}.")
    total_score += presentation_score
    presentation_count += 1
    command = input()


total_average = total_score / (jury_count * presentation_count)
print(f"Student's final assessment is {total_average :.2f}.")
