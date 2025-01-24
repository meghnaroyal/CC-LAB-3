import json
from typing import List
from cart import dao
from products import Product, get_product


class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> "Cart":
        """Create a Cart object from a dictionary."""
        return Cart(
            id=data["id"],
            username=data["username"],
            contents=[get_product(pid) for pid in json.loads(data["contents"])],
            cost=data["cost"],
        )


def get_cart(username: str) -> List[Product]:
    """Retrieve all products in the user's cart as a list of Product objects."""
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    # Parse and fetch products in a single step
    return [
        get_product(pid)
        for cart_detail in cart_details
        for pid in json.loads(cart_detail["contents"])
    ]


def add_to_cart(username: str, product_id: int) -> None:
    """Add a product to the user's cart."""
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int) -> None:
    """Remove a product from the user's cart."""
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str) -> None:
    """Delete the user's cart."""
    dao.delete_cart(username)
