
# Step 1: Project Setup
# File Name: data_manager.py
# ==========================================

# Step 2: Program Introduction
print("Welcome to Smart Contact & Inventory Manager")
print("=" * 43)

# Step-3: Contact Book (Dictionary)
contacts = {}

num_contacts = int(input("How many contacts do you want to add? "))


for i in range(num_contacts):
    print(f"\nEntering details for contact {i + 1}:")
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    contacts[name] = phone_number

# Step 4: Display All Contacts
print("\n--- Displaying All Contacts ---")

for name, phone_number in contacts.items():
    print(f"{name} - {phone_number}")

# Step 5: Update and Delete Contact
print("\n--- Update and Delete Contact ---")

update_name = input("Which contact do you want to update? ")

names_list = list(contacts.keys())
total_contacts = len(names_list)

for index in range(total_contacts):
  
    if names_list[index] == update_name:
        new_phone = input(f"Enter new phone number for {update_name}: ")
        contacts[update_name] = new_phone
        print("Updated successfully.")
        break 
else:
  
    print("Contact not found.")




delete_name = input("\nWhich contact do you want to delete? ")

deleted_value = contacts.pop(delete_name, "Not Found")

if deleted_value != "Not Found":
    print("Deleted successfully.")
else:
    print("Contact not found.")


# Step 6: Inventory Categories (Set)
print("\n--- Inventory Categories ---")
user_categories = set()

num_categories = int(input("How many product categories do you want to add? "))


for i in range(num_categories):
    category = input(f"Enter category #{i + 1}: ")
    user_categories.add(category)

print(f"Your categories: {user_categories}")

# Step 7: Set Operations
print("\n--- Set Operations ---")
# Sample set
sample_categories = {"electronics", "food", "clothes", "books"}
print(f"Sample categories: {sample_categories}")

# Union 
union_result = user_categories.union(sample_categories)
print(f"Union: {union_result}")

#difference

difference_result = user_categories.difference(sample_categories)
print(f"Difference: {difference_result}")

# Step 8: Nested Dictionary (Advanced)
print("\n--- Nested Inventory Dictionary ---")
inventory = {
    "Laptop": {"price": 50000, "stock": 10},
    "Phone": {"price": 30000, "stock": 20}
}

for product, details in inventory.items():
    print(f"Product: {product}")
    print(f"  Price: {details['price']}")
    print(f"  Stock: {details['stock']}")
