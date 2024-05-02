from collections import deque


def find_ducky(time):
    if 0 <= time <= 60:
        return "Darth Vader Ducky"
    elif 61 <= time <= 120:
        return "Thor Ducky"
    elif 121 <= time <= 180:
        return "Big Blue Rubber Ducky"
    elif 181 <= time <= 240:
        return "Small Yellow Rubber Ducky"
    elif time > 240:
        return None


time_needed = deque(map(int, input().split()))
programmers_tasks = list(map(int, input().split()))
duckies_dict = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while time_needed and programmers_tasks:
    current_programmer = time_needed[0] * programmers_tasks[-1]
    current_ducky = find_ducky(current_programmer)

    if current_ducky:
        duckies_dict[current_ducky] += 1
        time_needed.popleft()
        programmers_tasks.pop()

    else:
        programmers_tasks[-1] -= 2
        time_needed.append(time_needed.popleft())

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print("Darth Vader Ducky:", duckies_dict["Darth Vader Ducky"])
print("Thor Ducky:", duckies_dict["Thor Ducky"])
print("Big Blue Rubber Ducky:", duckies_dict["Big Blue Rubber Ducky"])
print("Small Yellow Rubber Ducky:", duckies_dict["Small Yellow Rubber Ducky"])
