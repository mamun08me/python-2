

inventory = []

n = int(input("How many items do you want to add to inventory?: "))

for i in range(n):
    
    if i == 0:
        ordinal_number = f"{i+1}st" 
    elif i == 1:
        ordinal_number = f"{i+1}nd" 
    elif i == 2:
        ordinal_number = f"{i+1}rd" 
    else:
        ordinal_number = f"{i+1}th" 
         
    print(f"\nEnter {ordinal_number} item's info: ")
    
  
    print("Select Item Type:")
    print("1. Mobile")
    print("2. Accessories")
    item_type_choice = input("Enter choice (1 or 2): ")
    
    if item_type_choice == "1":
        item_type = "Mobile"
        brand = input("Enter mobile brand name: ")
        model = input("Enter mobile model no: ")
        price = int(input("Enter unit price (Tk): "))       
        quantity = int(input("Enter quantity (Stock): "))     # স্টক সংখ্যা যোগ করা হলো
        
        # মোবাইল অবজেক্ট
        item = {
            "type": item_type,
            "brand": brand,
            "model": model,
            "price": price,
            "quantity": quantity
        }
        
    else:
        item_type = "Accessories"
        name = input("Enter accessory name : ")
        model = input("Enter accessory model: ")
        country = input("Enter manufacturing country: ")
        price = int(input("Enter unit price (Tk): "))       # হিসাবের সুবিধার জন্য float বা int
        quantity = int(input("Enter quantity (Stock): "))     # স্টক সংখ্যা যোগ করা হলো
       
        item = {
            "type": item_type,
            "name": name,
            "model": model,
            "country": country,
            "price": price,
            "quantity": quantity
        }
        
    inventory.append(item)

    # বর্তমান ইনভেনটরি লিস্ট প্রিন্ট করা
    print("\nCurrent Inventory List:")
    total_inventory_value = 0  
    
    for j in range(len(inventory)):
        current_item = inventory[j]
      
        item_total = current_item['price'] * current_item['quantity']
        total_inventory_value += item_total
        
        if current_item['type'] == "Mobile":
            print(f"{j+1}. {current_item['type']}\n{current_item['brand']} --{current_item['model']} "
                  f"\n- Price: {current_item['price']} Tk, \nQty: {current_item['quantity']} pcs \nTotal: {item_total} Tk")
        else:
            print(f"{j+1}. {current_item['type']}\n {current_item['name']} \nModel: {current_item['model']} \n Made in: {current_item['country']} "
                  f"\n- Price: {current_item['price']} Tk, \nQty: {current_item['quantity']} pcs (Total: {item_total} Tk)")
            
    # ইনভেনটরিতে থাকা সব আইটেমের মোট মূল্য প্রদর্শন
    print(f"\n---> Total Inventory Value: {total_inventory_value} Tk <---\n")

