first_upper = int(input())
second_upper = int(input())
third_upper = int(input())

for x in range(2, first_upper + 1, 2):
    for y in range(2, second_upper + 1):
        is_prime = True
        divisor = [2 - ]
        for divisor in range(2, int(y ** 0.5) + 1):
            if y % divisor == 0:
                is_prime = False
                break
        if is_prime:
            for z in range(2, third_upper + 1, 2):
                print(f"{x} {y} {z}")
