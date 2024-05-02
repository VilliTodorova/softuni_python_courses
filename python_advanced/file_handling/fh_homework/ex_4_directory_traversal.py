import os


def find_save_ext(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        path_file = os.path.join(dir_name, filename)

        if os.path.isfile(path_file):
            ext = filename.split(".")[-1]
            extensions[ext] = extensions.get(ext, []) + [filename]
        elif os.path.isdir(path_file) and not first_level:
            find_save_ext(path_file, first_level=True)


directory = input()
extensions = {}
result = []

try:
    find_save_ext(directory)
except FileNotFoundError:
    print("Dir is not valid!")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f"{extension}")

    for file in sorted(files):
        result.append(f"- - - {file}")

with open("files/report.txt", "w") as report_file:
    report_file.write("\n".join(result))
