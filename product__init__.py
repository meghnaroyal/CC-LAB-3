import json
from typing import List, Optional
from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> "Product":
        """Load a Product from a dictionary."""
        return Product(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            qty=data['qty']
        )


def list_products() -> List[Product]:
    """Return a list of all products."""
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Optional[Product]:
    """Fetch a product by its ID. Return None if the product doesn't exist."""
    product_data = dao.get_product(product_id)
    return Product.load(product_data) if product_data else None


def add_product(product: dict):
    """Add a new product to the inventory."""
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Update the quantity of a specific product."""
    if qty < 0:
        raise ValueError("Quantity cannot be negative")
    dao.update_qty(product_id, qty)
