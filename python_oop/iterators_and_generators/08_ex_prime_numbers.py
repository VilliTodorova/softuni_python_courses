def get_primes(nums):
    for n in nums:
        if n <= 1:
            continue

        for divisor in range(2, int(n ** 0.5) + 1):
            if n % divisor == 0:
                break

        else:
            yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
