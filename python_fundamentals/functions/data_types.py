def data_types(type_of_data, value):
    if type_of_data == "int":
        return int(value) * 2
    elif type_of_data == "real":
        return f'{(float(value) * 1.5):.2f}'
    elif type_of_data == "string":
        return f'${value}$'


type_of_data = input()
value = input()

print(data_types(type_of_data, value))
