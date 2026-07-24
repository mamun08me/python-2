import csv

# ১. 'contact.csv' থেকে ডেটা পড়া হচ্ছে (Read Mode)
with open("contact.csv", "r", encoding="utf-8") as infile:
    reader = csv.reader(infile, delimiter="\t")
    next(reader, None) # হেডার বাদ দেওয়া হলো
    
    # ২. 'cleaned_contact.csv' নামে নতুন ফাইলে লেখা হচ্ছে (Write Mode)
    with open("cleaned_contact.csv", "w", encoding="utf-8", newline="") as outfile:
        writer = csv.writer(outfile, delimiter=",") # নতুন ফাইলে কমা (,) দিয়ে সেভ হবে
        
        # নতুন ফাইলের কলামের নাম বা হেডার বসানো হলো
        writer.writerow(["Name", "Phone", "Address"])
        
        # ৩. লুপ চালিয়ে মেইন ফাইল থেকে পড়ে নতুন ফাইলে রাইট করা হচ্ছে
        for row in reader:
            if row:
                clean_row = [item.strip() for item in row if item.strip()]
                if len(clean_row) >= 3:
                    # সরাসরি নতুন ফাইলে লিখে দেওয়া হচ্ছে
                    writer.writerow(clean_row)

print("successfully write to the another file!")
