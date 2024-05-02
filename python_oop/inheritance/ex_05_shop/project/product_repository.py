from typing import List

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        prod = self.find(product_name)
        if prod:
            self.products.remove(prod)

    def __repr__(self):
        return "\n".join([f'{product.name}: {product.quantity}' for product in self.products])