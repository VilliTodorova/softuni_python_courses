total_failed_attempts = int(input())

failed_attempts = 0
total_attempts = 0
total_task_score = 0
last_task_name = ""
has_failed = True

while failed_attempts < total_failed_attempts:
    current_task_name = input()
    if current_task_name == "Enough":
        has_failed = False
        break
    current_score = int(input())
    if current_score <= 4:
        failed_attempts += 1
    total_task_score += current_score
    total_attempts += 1
    last_task_name = current_task_name

average_score = total_task_score / total_attempts
if has_failed:
    print(f"You need a break, {failed_attempts} poor grades.")
else:
    print(f"Average score: {average_score:.2f}\n"
          f"Number of problems: {total_attempts}\n"
          f"Last problem: {last_task_name}")
