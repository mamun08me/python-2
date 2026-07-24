# 2. Object-Oriented Programming (OOP)In OOP, 
# state (data) and behavior (functions) are combined into 
# custom objects. 
# We use Encapsulation to keep data safe inside the class.

class Item:
    """Represents a product item entity."""
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self) -> float:
        return self.price * self.quantity


class ShoppingCart:
    """Encapsulates items and cart behaviors."""
    TAX_RATE = 0.15  # Class constant

    def __init__(self):
        self.__items = []  # Private attribute (Encapsulation)

    def add_item(self, item: Item):
        self.__items.append(item)
        print(f"Added: {item.name} x{item.quantity}")

    def get_subtotal(self) -> float:
        return sum(item.get_total_price() for item in self.__items)

    def __apply_discount(self, subtotal: float, discount_code: str) -> float:
        """Private helper method."""
        if discount_code == "WELCOME10":
            return subtotal * 0.90
        return subtotal

    def checkout(self, discount_code: str = None):
        """Processes the state of the object to produce a receipt."""
        subtotal = self.get_subtotal()
        discounted_subtotal = self.__apply_discount(subtotal, discount_code)
        tax = discounted_subtotal * self.TAX_RATE
        total = discounted_subtotal + tax

        print("\n--- RECEIPT (OOP) ---")
        for item in self.__items:
            print(f"{item.name} (x{item.quantity}): ${item.get_total_price():.2f}")
        print(f"Subtotal: ${subtotal:.2f}")
        if discount_code:
            print(f"After Discount ({discount_code}): ${discounted_subtotal:.2f}")
        print(f"Tax (15%): ${tax:.2f}")
        print(f"Total: ${total:.2f}")


# --- EXECUTION ---
cart_obj = ShoppingCart()
cart_obj.add_item(Item("Laptop", 1200.00, 1))
cart_obj.add_item(Item("Mouse", 25.00, 2))
cart_obj.checkout(discount_code="WELCOME10")
