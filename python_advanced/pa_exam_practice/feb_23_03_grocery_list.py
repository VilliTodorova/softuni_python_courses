def shop_from_grocery_list(budget: int, products_to_buy: list, *product_data):

    for product_name, product_price in product_data:

        if not products_to_buy:
            break

        if product_name not in products_to_buy:
            continue

        if (budget - product_price) >= 0:
            budget -= product_price
            products_to_buy.remove(product_name)
        else:
            break

    if not products_to_buy:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(products_to_buy)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
