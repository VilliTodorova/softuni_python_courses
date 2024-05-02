electrons_count = int(input())
result = []
shell_count = 1

while True:

    electrons_in_shell = 2 * shell_count ** 2
    shell_count += 1

    if electrons_count - electrons_in_shell < 0:
        result.append(abs(electrons_count))
        electrons_count = 0
        break
    else:
        electrons_count -= electrons_in_shell
        result.append(electrons_in_shell)
    if electrons_count <= 0:
        break

print(result)
