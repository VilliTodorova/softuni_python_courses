people_waiting = int(input())
lift_state = input().split()

for course in lift_state:
    index = 0
    current_state = lift_state[index]
    if int(current_state) == 0:
        if people_waiting >= 4:
            lift_state[index].replace(current_state, '4')
            people_waiting -= 4
        elif people_waiting < 4:
            lift_state[index].replace(current_state, str(people_waiting))
    elif int(current_state) != 0:
        available_capacity = 4 - int(current_state)
        if people_waiting >= 4:
            lift_state[index].replace(current_state, '4')
            people_waiting -= available_capacity
        elif people_waiting < 4:
            lift_state[index].replace(current_state, str(people_waiting))
    index += 1
