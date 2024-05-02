from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:
        for task in self.tasks:
            if task.name == task_name:
                task.mark_completed()
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        count = sum(1 for task in self.tasks if task.completed)
        self.tasks = [task for task in self.tasks if not task.completed]
        return f"Cleared {count} tasks."

    def view_section(self) -> str:
        tasks_details = [task.details() for task in self.tasks]
        tasks_details_str = '\n'.join(tasks_details)
        return f"Section {self.name}:\n{tasks_details_str}"
