import math
people_count = int(input())
capacity = int(input())
courses = math.ceil(people_count / capacity)
print(courses)
