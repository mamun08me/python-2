contacts = [
    {"name": "Miftahul Islam", "phone": "01742855755"}, # GP
    {"name": "Abdur Rahman", "phone": "01812345678"},  # Robi
    {"name": "Fatema Khatun", "phone": "01923456789"}, # BL
    {"name": "Hasan Mahmud", "phone": "01612345678"},  # Airtel
    {"name": "Sadia Islam", "phone": "01552345678"},   # Teletalk
    {"name": "Kamrul Islam", "phone": "01798765432"},  # GP
    {"name": "Nusrat Jahan", "phone": "01876543210"},  # Robi
]

print("--- Contacts filter system---")
print("1. Grameenphone (017)")
print("2. Robi (018)")
print("3. Banglalink (019)")

while True:
    choice = input("which operation do you want to see? (1/2/3) or close enter to exit':q':")

    if choice != ":q":
            # শর্ত বা ফিল্টার কি (Prefix) ঠিক করা
            prefix = ""
            if choice == "1": prefix = "017"
            elif choice == "2": prefix = "018"
            elif choice == "3": prefix = "019"

            filtered_contacts = []
            
            # বিশুদ্ধ ফিল্টার লজিক
            for contact in contacts:
                if contact["phone"].startswith(prefix): # শর্ত মিললে লিস্টে ঢুকবে
                    filtered_contacts.append(contact)

            # রেজাল্ট প্রিন্ট
            print(f"\n--- no of filtered contacts ({len(filtered_contacts)}) ---")
            for contact in filtered_contacts:
                print(f"{contact['name']} - {contact['phone']}") # সিঙ্গেল কোটেশন ব্যবহার করা হয়েছে
    break