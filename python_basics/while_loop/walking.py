target_steps = 10000
total_steps = 0
command = ""
is_success = False

while command != "Going home":
    command = input()
    if command == "Going home":
        command = int(input())
        current_steps = command
        total_steps += current_steps
        if total_steps >= target_steps:
            is_success = True
        else:
            is_success = False
        break
    current_steps = int(command)
    total_steps += current_steps
    if total_steps >= target_steps:
        is_success = True
        break

leftover = total_steps - target_steps

if is_success:
    print(f"Goal reached! Good job!\n"
          f"{leftover} steps over the goal!")
else:
    print(f"{abs(leftover)} more steps to reach goal.")
