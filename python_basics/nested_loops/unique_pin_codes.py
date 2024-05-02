first_number = int(input())
second_number = int(input())
third_number = int(input())

for i in range(2, first_number + 1, 2):
    for j in range(2, second_number + 1):
        is_prime = True
        for divisor in range (2, int(j ** 0.5) + 1):
            if j % divisor == 0:
                is_prime = False
                break
        if is_prime:
            for k in range(2, third_number + 1, 2):
                print(f"{i} {j} {k}")
