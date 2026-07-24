# # ফাইল ওপেন করা
# file = open("demo.txt", "r")

# # সম্পূর্ণ ফাইল রিড করা
# print(file.read())


# # ফাইল ক্লোজ করা (খুবই গুরুত্বপূর্ণ)
# file.close()

# file = open("demo.txt", "r")
# print(file.read(5)) # প্রথম ৫টি ক্যারেক্টার প্রিন্ট করবে (Hello)
# file.close()

# # readline(): একটি করে একক লাইন পড়ে।
# # readlines(): সব লাইন পড়ে একটি লিস্ট (List) হিসেবে রিটার্ন করে।
# file = open("demo.txt", "r")

# # প্রথম লাইন
# print("Line 1:",file.readline() )

# # সব লাইন একসাথে লিস্ট হিসেবে
# file.seek(0) # ফাইলের শুরু থেকে রিড করার জন্য কার্সার ০-তে নেয়া
# lines = file.readlines()
# print("All Lines as List:", lines)
# file.close()
# # পদ্ধতি ৪: লুপ ব্যবহার করে লাইন বাই লাইন পড়া (সবচেয়ে ভালো উপায়)
# file = open("demo.txt", "r")
# for line in file:
#     print(line.strip()) # strip() দিয়ে লাইনের শেষের এক্সট্রা স্পেস/নিউলাইন সরানো হয়
# file.close()

# # ৪. ফাইলে রাইট বা অ্যাপেন্ড করা
# # Write মোড ('w') - নতুন ফাইল বা আগের ডেটা মুছে লেখা:
# file = open("output.txt", "w")
# file.write("This is a new file.\n")
# file.write("All previous data will be overwritten if this file existed.")
# file.close()
# # Append মোড ('a') - আগের ডেটার সাথে নতুন ডেটা যোগ করা:
# file = open("output.txt", "a")
# file.write("\nThis line is appended to the file.")
# file.close()

# # ৫. ফাইল ডিলিট করা (Deleting Files)
# # ফাইল ডিলিট বা মুছে ফেলার জন্য পাইথনের os (Operating System) মডিউল ব্যবহার করা হয়।

# import os

# # ফাইল ডিলিট করা
# if os.path.exists("output_1.txt"):
#     os.remove("output.txt")
#     print("File deleted successfully.")
# else:
#     print("File not found.")
    
    
# # ৬. ফাইল ক্লোজ করা এবং with স্টেটমেন্ট (Context Manager)
# # সবসময় ফাইল ব্যবহারের পর file.close() করা জরুরি। যদি কোনো কারণে প্রোগ্রামে এরর আসে, তাহলে ফাইলটি ওপেন অবস্থায় থেকে যেতে পারে এবং মেমোরি নষ্ট হতে পারে।

# # এই সমস্যা এড়ানোর জন্য পাইথনে with স্টেটমেন্ট বা Context Manager ব্যবহার করা হয়। with ব্লকের কাজ শেষ হলে পাইথন নিজে থেকেই ফাইলটি ক্লোজ করে দেয়, কোনো এক্সপ্লিসিট close() লিখতে হয় না।

# # উদাহরণ:
# with open("demo.txt", "r") as file:
#     data = file.read()
#     print(data)
#     # print(file.read())
# # এখানে ব্লক থেকে বের হওয়ার সাথে সাথে ফাইলটি স্বয়ংক্রিয়ভাবে ক্লোজ হয়ে গেছে।

# # ৭. CSV ফাইলের সাথে কাজ করা (Working with CSV)
# # CSV বা Comma Separated Values হলো টেবুলার ডেটা (যেমন এক্সেল শিট) সংরক্ষণের একটি জনপ্রিয় ফরম্যাট। পাইথনে বিল্ট-ইন csv মডিউল ব্যবহার করে খুব সহজে CSV ফাইল রিড ও রাইট করা যায়।

# # CSV ফাইল রিড করা (csv.reader):
# # ধরি, আমাদের কাছে students.csv নামের একটি ফাইল আছে:

# # Name,Age,Class
# # Miftahul,23,Python
# # Rahim,22,Java
# # Karim,24,Python
# # আমরা এটি এভাবে রিড করতে পারি:

# import csv

# with open("students.csv", mode="r", newline="", encoding="utf-8") as file:
#     csv_reader = csv.reader(file)
    
#     # প্রথম (Header) রোটি স্কিপ বা রিড করতে চাইলে:
#     header = next(csv_reader)
#     print("Headers:", header)
    
#     # বাকি ডেটা প্রিন্ট করা
#     for row in csv_reader:
#         print(f"Name: {row[0]}, Age: {row[1]}, Class: {row[2]}")


# # CSV ফাইলে রাইট করা (csv.writer):
# import csv

# data = [
#     ["Name", "Age", "Class"],
#     ["Miftahul", "23", "Python"],
#     ["Rahim", "22", "Java"],
#     ["Karim", "24", "Python"]
# ]

# with open("new_students.csv", mode="w", newline="", encoding="utf-8") as file:
#     csv_writer = csv.writer(file)
    
#     # একসাথে সব রো রাইট করা
#     csv_writer.writerows(data)
    
#     # অথবা একটি একটি করে রো রাইট করা:
#     # csv_writer.writerow(["Miftahul", "23", "Python"])

# print("CSV file created successfully!")


# ডিকশনারি ফরম্যাটে CSV রিড ও রাইট করা (Sleek & Recommended):
# DictReader এবং DictWriter ব্যবহার করলে ডেটাগুলোকে ডিকশনারি ফরম্যাটে সরাসরি ফিল্ডের নাম দিয়ে অ্যাক্সেস করা যায়।

# csv.DictReader ব্যবহার করে পড়া:
import csv

with open("students.csv", mode="r", newline="", encoding="utf-8") as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(f"Student: {row['Name']} studies {row['Class']}")
# csv.DictWriter ব্যবহার করে লেখা:
import csv

fieldnames = ["Name", "Age", "Class"]

with open("dict_students.csv", mode="w", newline="", encoding="utf-8") as file:
    dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # হেডার রাইট করা
    dict_writer.writeheader()
    
    # রো রাইট করা
    dict_writer.writerow({"Name": "Miftahul", "Age": "23", "Class": "Python"})
    dict_writer.writerow({"Name": "Rahim", "Age": "22", "Class": "Java"})