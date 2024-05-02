from collections import deque

matrix = [i.split() for i in input().split("|")]

# while matrix:
#     last_el = matrix.pop()
#     print(*last_el, end=" ")
#

print(*[' '.join(el) for el in matrix[::-1] if el])
