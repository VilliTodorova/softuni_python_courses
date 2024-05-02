command = input()
sum_primes = 0
sum_non_primes = 0

while command != "stop":
    current_number = int(command)
    is_prime = True

    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue

    for number in range(2, current_number):
        if current_number % number == 0:
            is_prime = False
            break

    if is_prime:
        sum_primes += current_number
    else:
        sum_non_primes += current_number

    command = input()

print(f"Sum of all prime numbers is: {sum_primes}\n"
      f"Sum of all non prime numbers is: {sum_non_primes}")
