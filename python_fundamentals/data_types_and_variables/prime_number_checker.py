import math

your_num = int(input())
is_prime = True
if your_num <= 1:
    is_prime = False
for i in range(2, int(math.sqrt(your_num)) + 1):
    if your_num % i == 0:
        is_prime = False
        break

if is_prime:
    print("True")
else:
    print("False")
