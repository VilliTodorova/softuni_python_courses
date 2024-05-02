time_sequence = input().split()
middle_index = (len(time_sequence) - 1) // 2
left_side = time_sequence[:middle_index]
right_side = time_sequence[middle_index + 1:][::-1]

sum_time_left = 0
sum_time_right = 0
winner = ""
winner_time = 0

for i in left_side:
    current_time_left = int(i)
    sum_time_left += current_time_left
    if current_time_left == 0:
        sum_time_left *= 0.8
for j in right_side:
    current_time_right = int(j)
    sum_time_right += current_time_right
    if current_time_right == 0:
        sum_time_right *= 0.8

if sum_time_left < sum_time_right:
    winner = "left"
    winner_time = sum_time_left
elif sum_time_left > sum_time_right:
    winner = "right"
    winner_time = sum_time_right

print(f'The winner is {winner} with total time: {winner_time:.1f}')
