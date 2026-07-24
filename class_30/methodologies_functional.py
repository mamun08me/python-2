# 3. Functional Programming (Pure Functions & Pipelines)
# In Functional Programming, data is immutable 
# (never modified in place).
# Instead of changing a global list,
# functions take a dataset, process it, 
# and return a brand new dataset.
# We use Python's higher-order tools like lambda, map, and reduce.

from functools import reduce

# --- IMMUTABLE DATA DATA STRUCTURES (Tuple of Dicts) ---
# We avoid modifying this setup directly
initial_cart = (
    {"name": "Laptop", "price": 1200.00, "quantity": 1},
    {"name": "Mouse", "price": 25.00, "quantity": 2},
)

TAX_RATE = 0.15

# --- PURE FUNCTIONS ---
# Function 1: Transforms data to find item totals
get_item_total = lambda item: item["price"] * item["quantity"]

# Function 2: Calculates total sum using reduce (Functional Loop)
calculate_subtotal = lambda cart_data: reduce(lambda acc, item: acc + get_item_total(item), cart_data, 0.0)

# Function 3: Pure conditional transformation
apply_discount = lambda subtotal, code: subtotal * 0.90 if code == "WELCOME10" else subtotal

# Function 4: Calculates tax and final total as an immutable tuple output
calculate_final_bill = lambda subtotal, code: (
    apply_discount(subtotal, code),                                     # Discounted price
    apply_discount(subtotal, code) * TAX_RATE,                          # Tax
    apply_discount(subtotal, code) + (apply_discount(subtotal, code) * TAX_RATE) # Grand Total
)

def print_functional_receipt(cart_data, discount_code=None):
    """A display function wrapper that pipes the pure computations together."""
    subtotal = calculate_subtotal(cart_data)
    discounted, tax, total = calculate_final_bill(subtotal, discount_code)
    
    print("\n--- RECEIPT (Functional) ---")
    # Using map() to apply a function over a collection cleanly
    list(map(lambda item: print(f"{item['name']} (x{item['quantity']}): ${get_item_total(item):.2f}"), cart_data))
    
    print(f"Subtotal: ${subtotal:.2f}")
    if discount_code:
        print(f"After Discount ({discount_code}): ${discounted:.2f}")
    print(f"Tax (15%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

# --- EXECUTION ---
# Notice how we pass data strictly through function arguments
print_functional_receipt(initial_cart, discount_code="WELCOME10")
