def calculate_average_happiness(employee_happiness, improvement_factor):

    employee_happiness = list(map(int, employee_happiness))
    employee_happiness = [employee_score * improvement_factor for employee_score in employee_happiness]
    average_happiness = sum(employee_happiness) / len(employee_happiness)
    happy_employees = [happy for happy in employee_happiness if happy >= average_happiness]

    if len(happy_employees) >= len(employee_happiness) / 2:
        print(f"Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are happy!")
    else:
        print(f'Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are not happy!')


employee_happiness = input().split()
improvement_factor = int(input())

calculate_average_happiness(employee_happiness, improvement_factor)
