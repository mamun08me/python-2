#1. Procedural Programming (Step-by-Step Execution)
# In procedural programming, data is stored in simple structures (like lists and dicts),
# and functions directly modify or process that data globally.


# --- GLOBAL DATA ---
cart = []
TAX_RATE = 0.15  # 15% Tax

# --- PROCEDURAL FUNCTIONS ---
def add_item_to_cart(name, price, quantity):
    """Directly modifies the cart data structure."""
    item = {"name": name, "price": price, "quantity": quantity}
    cart.append(item)
    print(f"Added: {name} x{quantity}")

def calculate_subtotal():
    """Loops through global data to calculate a sum."""
    subtotal = 0.0
    for item in cart:
        subtotal += item["price"] * item["quantity"]
    return subtotal

def apply_discount(subtotal, discount_code):
    """Applies conditional logic to a raw value."""
    if discount_code == "WELCOME10":
        return subtotal * 0.90  # 10% off
    return subtotal

def print_receipt(discount_code=None):
    """Executes a linear sequence of printing steps."""
    subtotal = calculate_subtotal()
    discounted_subtotal = apply_discount(subtotal, discount_code)
    tax = discounted_subtotal * TAX_RATE
    total = discounted_subtotal + tax
    
    print("\n--- RECEIPT (Procedural) ---")
    for item in cart:
        print(f"{item['name']} (x{item['quantity']}): ${item['price'] * item['quantity']:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    if discount_code:
        print(f"After Discount ({discount_code}): ${discounted_subtotal:.2f}")
    print(f"Tax (15%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

# --- EXECUTION ---
add_item_to_cart("Laptop", 1200.00, 1)
add_item_to_cart("Mouse", 25.00, 2)
print_receipt(discount_code="WELCOME10")
