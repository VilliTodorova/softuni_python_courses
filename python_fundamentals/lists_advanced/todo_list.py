# def sort_todo_tasks():
#     todo_tasks = []
#
#     while True:
#         command = input()
#
#         if command == "End":
#             break
#
#         todo_tasks.append(command)
#
#     sorted_tasks = sorted(todo_tasks, key=lambda x: int(x.split('-')[0]))
#     return [note.split('-')[1] for note in sorted_tasks]
#
#
# result = sort_todo_tasks()
# print(result)


tasks = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    todo_task = command.split('-')
    current_task = todo_task[1]
    priority = int(todo_task[0]) - 1
    tasks.pop(priority)
    tasks.insert(priority, current_task)

result = [element for element in tasks if element != 0]
print(result)
