path = input().split("\\")
file = path[-1].split('.')

file_name, extension = file[0], file[1]

print(f'File name: {file_name}\nFile extension: {extension}')
