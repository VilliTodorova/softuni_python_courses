people_waiting = int(input())
initial_state = list(map(int, input().split()))
total_wagons = len(initial_state)

for i in range(total_wagons):
    while initial_state[i] < 4 and people_waiting > 0:
        initial_state[i] += 1
        people_waiting -= 1

# Check the final state and print the appropriate message
if people_waiting == 0 and all(wagon == 4 for wagon in initial_state):
    print(" ".join(map(str, initial_state)))

elif people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(map(str, initial_state)))
else:
    print("The lift has empty spots!")
    print(" ".join(map(str, initial_state)))
