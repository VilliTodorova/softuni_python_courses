command = input().split(' -> ')
companies_dict = {}

while command[0] != 'End':
    company_name, employee_id = command[0], command[1]

    if company_name not in companies_dict:
        companies_dict[company_name] = [employee_id]
    else:
        if employee_id not in companies_dict[company_name]:
            companies_dict[company_name].append(employee_id)

    command = input().split(' -> ')

for companies in companies_dict:
    print(companies)
    for id in companies_dict[companies]:
        print(f'-- {id}')
