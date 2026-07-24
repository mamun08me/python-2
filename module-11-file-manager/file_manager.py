import os
import random
from datetime import datetime

# Step 2: Program Introduction
print("====================================")
print("Welcome to Smart File-Based Manager")
print("====================================")

# Step 3: Menu System
while True:
    print("\n--- Smart File-Based Manager Menu ---")
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. Add new note")
    print("4. View all notes")
    print("5. Exit")

    choice = input("\nChoose an option (1-5): ").strip()

    # Step 4: File Writing (Expenses)
    if choice == "1":
        title = input("Enter expense title: ").strip()
        amount = input("Enter amount: ").strip()

        unique_id = random.randint(1000, 9999)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("expenses.csv", "a", encoding="utf-8") as file:
            file.write(f"{unique_id},{current_time},{title},{amount}\n")
        print(f" Expense saved successfully! in (ID: {unique_id})")

    # Step 5: File Reading (Expenses)
    elif choice == "2":
     
        if not os.path.exists("expenses.csv"):
            print("No records found yet.")
        else:
            print(
                f"\n{'ID':<6} | {'Date & Time':<20} | {'Title':<15} | {'Amount':<10}"
            )
            print("-" * 60)
            with open("expenses.csv", "r", encoding="utf-8") as file:
                for line in file:
                    if line.strip():
                        uid, d_time, tit, amt = line.strip().split(",")
                        print(
                            f"{uid:<6} | {d_time:<20} | {tit:<15} | {amt:<10}"
                        )

    # Step 6: Notes File System
    elif choice == "3":
        note_content = input("Enter your note: ").strip()

        unique_id = random.randint(1000, 9999)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("notes.txt", "a", encoding="utf-8") as file:
            file.write(
                f"ID: {unique_id} | Date: {current_time}\nNote: {note_content}\n"
            )
            file.write("-" * 40 + "\n")
        print(f" Note saved successfully in (ID: {unique_id})")

    elif choice == "4":
        if not os.path.exists("notes.txt"):
            print(" No records found yet.")
        else:
            print("\n--- All Notes ---")
            with open("notes.txt", "r", encoding="utf-8") as file:
                print(file.read())

    # Exit Option
    elif choice == "5":
        print("\nThank you for using Smart File-Based Manager. Goodbye!")
        break
    else:
        print("Invalid option! Please choose between 1 and 5.")
        
