def swap(num_array, index1, index2):
    num_array[index1], num_array[index2] = num_array[index2], num_array[index1]

    return num_array


def multiply(num_array, index1, index2):
    new_num = num_array[index1] * num_array[index2]
    num_array[index1] = new_num

    return num_array


def decrease(num_array):
    for i in range(len(num_array)):
        num_array[i] -= 1

    return num_array


num_array = [int(num) for num in input().split()]
command = input().split()

while command[0] != 'end':
    if command[0] == 'swap':
        index1, index2 = int(command[1]), int(command[2])
        num_array = swap(num_array, index1, index2)
    elif command[0] == 'multiply':
        index1, index2 = int(command[1]), int(command[2])
        num_array = multiply(num_array, index1, index2)
    elif command[0] == 'decrease':
        num_array = decrease(num_array)

    command = input().split()

num_array = list(map(str, num_array))
print(', '.join(num_array))
