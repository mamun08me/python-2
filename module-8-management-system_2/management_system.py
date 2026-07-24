
student_names = []
student_scores = []
contact_book = {}
product_categories = set()
vote_counts={}
nested_student_marks = {
    "John": [80, 75, 90],
    "Alex": [70, 85, 88]
}

while True:
   
    # STEP 2: PROGRAM INTRODUCTION & MENU
   
    print("="*50)
    print("Welcome to Smart School Management & Voting Analysis System")
    print("="*60)
    print("1. Add Student Scores")
    print("2. View Score Summary")
    print("3. Manage Contacts/Inventory")
    print("4. Run Voting System")
    print("5. Exit")
    
    
    choice = input("Enter your choice (1-5): ").strip()
    
    # STEP 3: STUDENT SCORE TRACKER

    if choice == '1':
        print("\n--- Add Student Scores ---")
    
    
        while True:
            num_input = input("How many students to enter? ").strip()
            if num_input == "":
                print("Input cannot be empty!")
                continue
            is_valid_number = True
            for char in num_input:
                if char not in "0123456789": 
                    is_valid_number = False
                    break
                    
            if is_valid_number and int(num_input) > 0:
                num_students = int(num_input)
                break
            print("Invalid input! Please enter a valid positive number.")

      
        for i in range(num_students):
            name = input(f"Enter name of student {i+1}: ").strip()
            
            while True:
                score_input = input(f"Enter score for {name}: ").strip()
                
                if score_input == "":
                    print("Score cannot be empty!")
                    continue
                    
                is_valid_score = True
                dot_count = 0 
                
                for char in score_input:
                    if char == '.':
                        dot_count += 1
                    elif char not in "0123456789":
                        is_valid_score = False
                        break
                
                if is_valid_score and dot_count <= 1:
                    score = float(score_input)
                    break
                print("Invalid score! Please enter a valid numerical value (e.g., 85 or 92.5).")
                
           
            student_names.append(name)
            student_scores.append(score)
        
        # Display all students with scores
        print("\nRegistered Students and Scores:")
        for i in range(len(student_names)):
            print(f"Student: {student_names[i]} | Score: {student_scores[i]}")
        
        # Convert score list into a Tuple and print it
        scores_tuple = tuple(student_scores)
        print(f"Score Tuple: {scores_tuple}")

        
        # STEP 4 & 10: SCORE ANALYSIS & NESTED LOOP
       
    elif choice == '2':
            print("\n--- View Score Summary ---")
            
            # Step 4: Basic Analysis (With using DSA)
            if not student_scores:
                print(" No basic scores found. Please add scores from Menu-1")
            else:
                highest_score = student_scores[0]
                lowest_score = student_scores[0]
                total_score = 0
                
                for score in student_scores:
                    if score > highest_score:
                        highest_score = score
                    if score < lowest_score:
                        lowest_score = score
                    total_score += score
                    
                average_score = total_score / len(student_scores)
                
                print("\nStep 4: Basic Analysis Results")
                print(f"Highest Score: {highest_score}")
                print(f"Lowest Score : {lowest_score}")
                print(f"Average Score: {average_score}")
                
            # Step 10: Advanced Challenge (Nested Loops)
            print("\nStep 10: Advanced Subject Marks Analysis (Nested Loops)")
            for student in nested_student_marks:
                marks_list = nested_student_marks[student]
                print(f"Student: {student}")
                
                total_subject_score = 0
                subject_count = 1
                
               
                for mark in marks_list:
                    print(f" Subject {subject_count} Score: {mark}")
                    total_subject_score += mark
                    subject_count += 1
                    
                print(f"Total Score for {student}: {total_subject_score}")

        # STEP 5 & 6: CONTACT BOOK & SET MANAGEMENT
        
    elif choice == '3':
            print("\n--- Manage Contacts & Inventory ---")
            print("A. Contact Book CRUD Operations (Step 5)")
            print("B. Unique Category Management (Step 6)")
            sub_choice = input("Select Option (A or B): ").strip().upper()
            if sub_choice == 'A':
                    # Step 5: Dictionary CRUD
                    print("\n--- Contact Book Menu ---")
                    action = input("Choose Action (add / update / delete / view): ").strip().lower()
                    
                    if action == 'add':
                        name = input("Enter contact name: ").strip()
                        phone = input("Enter phone number: ").strip()
                        contact_book[name] = phone
                        print(f"Record added: {name} -> {phone}")
                        
                    elif action == 'update':
                        name = input("Enter name to update: ").strip()
                        if name in contact_book:
                            phone = input("Enter new phone number: ").strip()
                            contact_book[name] = phone
                            print("Record updated successfully.")
                        else:
                            print("Record not found!")
                            
                    elif action == 'delete':
                        name = input("Enter name to delete: ").strip()
                        if name in contact_book:
                            del contact_book[name]
                            print("Record deleted successfully.")
                        else:
                            print("Record not found!")
                            
                    elif action == 'view':
                        print("\nDisplaying Records using .items():")
                        if not contact_book:
                            print("Contact book is empty.")
                        else:
                            for name, phone in contact_book.items():
                                print(f"Name: {name} → Phone: {phone}")
                    else:
                        print("Invalid Action!")
                        
                           
            elif sub_choice == 'B':
                # Step 6: Unique Category Management using Sets
                    print("\n--- Unique Category Management ---")
                    cat_input = input("Enter product categories to add (separated by comma): ")
                    
                    # --- Set 1: 
                    current_cat = ""
                    for char in cat_input:
                        if char == ',':
                            clean_cat = current_cat.strip()
                            if clean_cat: 
                                product_categories.add(clean_cat)
                            current_cat = "" 
                        else:
                            current_cat += char 
                            
                    
                    if current_cat.strip():
                        product_categories.add(current_cat.strip())
                        
                    print(f"Set 1 (Unique Values): {product_categories}")
                    
            
                    set2_input = input("\nEnter categories for Set 2 (separated by comma): ")
                    set2 = set()
                    
                    current_cat = ""
                    for char in set2_input:
                        if char == ',':
                            clean_cat = current_cat.strip()
                            if clean_cat:
                                set2.add(clean_cat)
                            current_cat = ""
                        else:
                            current_cat += char
                            
                    if current_cat.strip():
                        set2.add(current_cat.strip())
                    
                    print(f"Set 2 Values: {set2}")
                    print(f"Union: {product_categories.union(set2)}")
                    print(f"Difference: {product_categories.difference(set2)}")
                
         
            # STEP 7, 8 & 9: VOTING & SEARCH SYSTEM
           
    elif choice == '4':
            print("\n--- Run Voting System & Searching ---")
            
            while True:
                num_input = input("Enter number of voters: ").strip()
                
                if num_input == "":
                    print("Input cannot be empty!")
                    continue
                    
                
                is_valid_number = True
                for char in num_input:
                    if char not in "0123456789":  
                        break
                        
                if is_valid_number and int(num_input) > 0:
                    num_voters = int(num_input)
                    break
                print("Invalid input! Please enter a valid positive number.")
            
            votes = []
            for i in range(num_voters):
                v_input = input(f"Voter {i+1}, enter candidate name: ").strip().upper()
                votes.append(v_input)
                
            # Step 7: Frequency Counter using Dictionary
            vote_counts = {}
            for candidate in votes:
                if candidate in vote_counts:
                    vote_counts[candidate] += 1
                else:
                    vote_counts[candidate] = 1
            
            print("\nVote Results Frequency:")
            for candidate, count in vote_counts.items():
                print(f"Candidate {candidate}: {count} votes")
                
            # Step 8: Winner Detection 
            if vote_counts:
                winner = None
                max_votes = -1
                for candidate, count in vote_counts.items():
                    if count > max_votes:
                        max_votes = count
                        winner = candidate
                print(f"\n Winner is Candidate {winner}")
                    
                # Step 9: Searching Feature 
                print("\n--- Step 9: Search Feature ---")
                search_query = input("Enter name to search (Student/Contact/Candidate): ").strip()
                found = False
                
                # Search in Student List 
                if search_query in student_names:
                    idx = student_names.index(search_query)
                    print(f"[Found in Students] {search_query} scored {student_scores[idx]}")
                    found = True
                    
                #Search in Contact Dictionary 
                if search_query in contact_book:
                    print(f"[Found in Contacts] {search_query}'s Phone: {contact_book[search_query]}")
                    found = True
                    
                # Search in Candidate Dictionary 
               
                if search_query.upper() in vote_counts:
                    print(f"[Found in Candidates] Candidate {search_query.upper()} received {vote_counts[search_query.upper()]} votes")
                    found = True
                    
                if not found:
                    print("Record not found")
        
    # STEP 2: EXIT PROGRAM
       
    elif choice == '5':
        print("\nExiting the system. Thank you!")
        break    
            
    else:
        print("Invalid choice! Please enter a number between 1 and 5")   