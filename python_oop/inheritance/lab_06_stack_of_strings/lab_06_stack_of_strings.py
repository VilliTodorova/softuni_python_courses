from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return not self.data

    def __str__(self):
        reversed_result = reversed(self.data)
        return f'[{", ".join(reversed_result)}]'
