products_info = input().split()
stock = {}

for i in range(0, len(products_info), 2):
    key = products_info[i]
    value = products_info[i + 1]
    stock[key] = int(value)

searched_products = input().split()
for product in searched_products:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
