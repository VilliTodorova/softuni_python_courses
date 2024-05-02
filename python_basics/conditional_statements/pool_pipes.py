from math import ceil, floor

pool_volume = int(input())
first_pipe_debit = int(input())
second_pipe_debit = int(input())
hours_absent = float(input())

# •	До колко се е запълнил басейна и коя тръба с колко процента е допринесла.
# "The pool is {запълненост на басейна в проценти}% full. Pipe 1: {процент вода от първата тръба}%.
# Pipe 2: {процент вода от втората тръба}%."
# Aко басейнът се е препълнил – с колко литра е прелял за даденото време.
# o	"For {часовете, които тръбите са пълнили вода} hours the pool overflows with {литрите вода в повече} liters."

capacity_first_pipe = first_pipe_debit * hours_absent
capacity_second_pipe = second_pipe_debit * hours_absent
total_filling_capacity = capacity_first_pipe + capacity_second_pipe

percentage_full = (total_filling_capacity / pool_volume) * 100
percentage_first_pipe = (capacity_first_pipe / total_filling_capacity) * 100
percentage_second_pipe = (capacity_second_pipe / total_filling_capacity) * 100
overflow_litres = total_filling_capacity - pool_volume

if total_filling_capacity <= pool_volume:
    print(f'The pool is {percentage_full :.2f}% full. Pipe 1: {percentage_first_pipe :.2f}%. '
          f'Pipe 2: {percentage_second_pipe :.2f}%.')
else:
    print(f'For {hours_absent} hours the pool overflows with {overflow_litres :.2f} liters.')
