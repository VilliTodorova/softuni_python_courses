def grocery_store(**product_data):
    products = sorted(product_data.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    return "\n".join(f"{prod}: {quantity}" for prod, quantity in products)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
