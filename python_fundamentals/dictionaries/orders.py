products = {}

while True:
    input_line = input()
    if input_line == "buy":
        break

    product_info = input_line.split()
    product_name, product_price, product_quantity = product_info[0], float(product_info[1]), int(product_info[2])

    if product_name in products:
        # Product already exists, update price and quantity
        products[product_name] = (product_price, products[product_name][1] + product_quantity)
    else:
        # Product doesn'project exist, add it with initial quantity and price
        products[product_name] = (product_price, product_quantity)

# Print the information about each product
for product_name, (product_price, product_quantity) in products.items():
    total_price = product_price * product_quantity
    print(f"{product_name} -> {total_price:.2f}")
