def check_if_perfect(your_num):
    divisors_sum = 0
    if your_num <= 0:
        print("It's not so perfect.")
        return False
    for divisor in range(1, your_num):
        if your_num % divisor == 0:
            divisors_sum += divisor

    if your_num == divisors_sum:
        print("We have a perfect number!")
        return True
    else:
        print("It's not so perfect.")
        return False


your_num = int(input())
check_if_perfect(your_num)
