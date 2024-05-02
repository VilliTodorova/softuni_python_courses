integer_a = int(input())
integer_b = int(input())

before_a = integer_a
before_b = integer_b
integer_a = before_b
integer_b = before_a
print(f'Before:\na = {before_a}\nb = {before_b}')
print(f'After:\na = {integer_a}\nb = {integer_b}')
