contacts = []

n = int(input("How many contacts do you want to input? "))

for i in range(n):
    # সঠিক অর্ডিনাল নাম্বার (1st, 2nd, 3rd...) নির্ধারণ
    if i == 0:
        ordinal_number = f"{i+1}st" 
    elif i == 1:
        ordinal_number = f"{i+1}nd" 
    elif i == 2:
        ordinal_number = f"{i+1}rd" 
    else:
        ordinal_number = f"{i+1}th" 
         
    # এখানে ordinal_number ব্যবহার করা হয়েছে
    print(f"\nEnter {ordinal_number} contact's info: ")
    
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contact1 = {
        "name": name,
        "phone": phone
    }
    contacts.append(contact1)

    # ভেতরের লুপের জন্য 'j' ব্যবহার করা হয়েছে এবং ভেতরের কোটেশন সিঙ্গেল ('') করা হয়েছে
    print("\nCurrent Contact List:")
    for j in range(len(contacts)):
        print(f"{j+1}. {contacts[j]['name']}: {contacts[j]['phone']}")
