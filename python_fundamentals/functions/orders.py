product = input()
quantity = int(input())


def calculate_total(product, quantity):
    if product == 'coffee':
        return f'{1.50 * quantity:.2f}'
    elif product == 'coke':
        return f'{1.40 * quantity:.2f}'
    elif product == 'water':
        return f'{1.00 * quantity:.2f}'
    elif product == 'snacks':
        return f'{2.00 * quantity:.2f}'


result = calculate_total(product, quantity)
print(result)
