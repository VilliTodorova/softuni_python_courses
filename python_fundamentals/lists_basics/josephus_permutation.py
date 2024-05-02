circle_sequence = input().split()
step = int(input())
executed = []
index = 0
circle_sequence = [int(person) for person in circle_sequence]

while len(circle_sequence) > 0:
    index = (index + step - 1) % len(circle_sequence)
    executed.append(circle_sequence.pop(index))

result = str(executed).replace(" ", "")
print(result)