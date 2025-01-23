import json
from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    products = dao.list_products()
    # Optimized using list comprehension for efficient object creation
    return [Product.load(product) for product in products]


def get_product_details(product_ids: list[int]) -> list[Product]:
    # Optimized by fetching all products in a single batch query
    products = dao.get_products_bulk(product_ids)
    return [Product.load(product) for product in products]
