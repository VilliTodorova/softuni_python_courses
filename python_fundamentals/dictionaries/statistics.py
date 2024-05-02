stock = {}

while True:
    product_info = input().split(': ')

    if product_info[0] == 'statistics':
        break

    key = product_info[0]
    value = int(product_info[1])
    if key not in stock:
        stock[key] = 0
    stock[key] += value

print('Products in stock:')
for (key, value) in stock.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(stock.keys())}')
print(f'Total Quantity: {sum(stock.values())}')
