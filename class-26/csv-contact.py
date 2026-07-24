
# import csv
# with open("contact.csv", "r") as file1:
#     reader = csv.reader(file1)
#     # print(reader[0])
#     # print(type(reader))
#     i = 0
#     for row in reader:
#         # print(row)
#         # print(type(row))
#         if i != 0:
#             print(f"Name: {row[0]}\tPhone: {row[1]}\tAddress: {row[2]}")
#         i += 1
   
import csv

with open("contact.csv", "r", encoding="utf-8") as file1:
    # delimiter="\t" দিয়ে পাইথনকে বলা হলো কলামগুলো ট্যাব দিয়ে আলাদা করা
    reader = csv.reader(file1, delimiter="\t")
    next(reader, None)  # হেডার বাদ দেওয়া হলো
    
    
    for row in reader:
        if row:  # ফাঁকা লাইন এড়ানোর জন্য
            # অনেক সময় একাধিক ট্যাব থাকলে খালি উপাদান তৈরি হয়, তাই সেগুলো ফিল্টার করা হলো
            clean_row = [item.strip() for item in row if item.strip()]
            
            # নিশ্চিত হওয়া হচ্ছে যে অন্তত ৩টি কলামের ডেটা আছে
            if len(clean_row) >= 3:
                print(f"Name: {clean_row[0]:<20} Phone: {clean_row[1]:<15} Address: {clean_row[2]}")
                
