
contacts = [
    {
        "name": "Miftahul Islam",
        "phone": "01742855755"
    },
    {
        "name": "Abdur Rahman",
        "phone": "01812345678"
    },
    {
        "name": "Fatema Khatun",
        "phone": "01923456789"
    },
    {
        "name": "Hasan Mahmud",
        "phone": "01612345678"
    },
    {
        "name": "Sadia Islam",
        "phone": "01552345678"
    },
    {
        "name": "Kamrul Islam",
        "phone": "01798765432"
    },
    {
        "name": "Nusrat Jahan",
        "phone": "01876543210"
    },
    {
        "name": "Rakib Ahmed",
        "phone": "01987654321"
    },
    {
        "name": "Tania Akter",
        "phone": "01676543210"
    },
    {
        "name": "Mahbub Alam",
        "phone": "01511223344"
    },
    {
        "name": "Shuvo Das",
        "phone": "01712398765"
    },
    {
        "name": "Jannatul Ferdous",
        "phone": "01823498765"
    },
    {
        "name": "Arif Hossain",
        "phone": "01934598765"
    }
]


search_term = ""

while True:
    search_term = input("Enter a phone number or name to search: ")
    if search_term == ":q":
        print("Exiting.....")
        break
        
    found_contacts = []
    
    for contact in contacts:
        # lower() ব্যবহার করা হয়েছে যেন ছোট হাতের বা বড় হাতের অক্ষরের পার্থক্য না হয়
        if (search_term.lower() in contact["name"].lower()) or (search_term in contact["phone"]):
            found_contacts.append(contact)
            
    if found_contacts:
        print(f"Total {len(found_contacts)} contact(s) found:")
        for contact in found_contacts:
            print(f" - {contact['name']}: {contact['phone']}")
    else:
        print("contact not found")
