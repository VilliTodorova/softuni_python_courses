product_info = input().split()
current_stock = {}

for i in range(0, len(product_info), 2):
    key = product_info[i]
    value = product_info[i + 1]
    current_stock[key] = int(value)

print(current_stock)
