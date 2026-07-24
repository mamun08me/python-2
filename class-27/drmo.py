
from datetime import datetime
incomes=[]

def add_income():
    # Auto-generated attributes
    global incomes
    income_id = len(incomes) + 1 
    date_created = datetime.now().strftime("%Y-%m-%d")
    date_updated = datetime.now().strftime("%Y-%m-%d")
    # User inputs
    category = input("Category: ")
    short_description = input("Short Description: ")
    description = input("Description: ")
    amount = input("Amount: ")
    date = input("Date: ")

    incomes.append({
        "income_id": income_id,
        "category": category,
        "short_description": short_description,
        "description": description,
        "amount": amount,
        "date": date,
        "date_created": date_created,
        "date_updated": date_updated
    })
    print("Income added successfully")
def add_income():