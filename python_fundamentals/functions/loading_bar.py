def loading_bar(your_percent):
    current_bar = []
    multiplier_percent = int(your_percent / 10)
    multiplier_dots = 10 - multiplier_percent

    # add % to the loading bar representing the actual percentage of completion
    for i in range(multiplier_percent):
        current_bar.append("%")

    # prepare the actual output string of the loading bar in the needed format
    loading_bar_str = f'[{"".join(current_bar)}{"." * multiplier_dots}]'

    # make necessary checks in order to provide the requested output message along with the loading bar
    if your_percent < 100:
        print(f'{your_percent}% {loading_bar_str}\n'
              f'Still loading...')
    else:
        print(f'{your_percent}% Complete!\n{loading_bar_str}')


your_percent = int(input())
loading_bar(your_percent)
