
# text = "hello WORLD"

# print(text.upper())       # আউটপুট: HELLO WORLD
# print(text.lower())       # আউটপুট: hello world
# print(text.capitalize())  # আউটপুট: Hello world
# print(text.title())       # আউটপুট: Hello World
# print(text.swapcase())    # আউটপুট: HELLO world


# text = "Python is amazing and Python is easy."

# print(text.count("Python"))     # আউটপুট: 2
# print(text.find("amazing"))     # আউটপুট: 10 (ইনডেক্স ১০ নম্বর পজিশনে আছে)
# print(text.find("Java"))        # আউটপুট: -1 (কারণ Java স্ট্রিংয়ে নেই)
# print(text.startswith("Python"))# আউটপুট: True
# print(text.endswith("easy."))   # আউটপুট: True

# spaced_text = "   Hello Python   "
# print(spaced_text.strip())   # আউটপুট: "Hello Python"
# print(spaced_text.lstrip())  # আউটপুট: "Hello Python   "

# text = "I love Java"
# print(text.replace("Java", "Python")) # আউটপুট: I love Python

# print(spaced_text.strip())
# print(text.replace("I","We"))

# split() এর উদাহরণ
# fruits = "apple, banana, cherry"
# fruits_list = fruits.split(", ")
# print(fruits_list)  # আউটপুট: ['apple', 'banana', 'cherry']

# # join() এর উদাহরণ
# words = ['Python', 'is', 'fun']
# sentence = " ".join(words)
# print(sentence)     # আউটপুট: Python is fun

# words_2=['I', 'love', 'Bangladesh']
# sentence_2=" ".join(words_2)
# print(sentence_2)

# print("Python_3".isalnum()) # আউটপুট: True (অক্ষর ও সংখ্যা আছে)
# print("12345".isdigit())   # আউটপুট: True (সব সংখ্যা)
# print("Hello".isalpha())   # আউটপুট: True (সব অক্ষর)
# print("Hello World".isalpha()) # আউটপুট: False (মাঝে স্পেস আছে)
print("   ".isspace())  
# Output: True

# উদাহরণ ২: ট্যাব এবং নতুন লাইন
print("\t\n".isspace())  
# Output: True

# উদাহরণ ৩: খালি স্ট্রিং
print("".isspace())  
# Output: False

# উদাহরণ ৪: সাধারণ টেক্সট এবং স্পেস
print("Hello World".isspace())  
# Output: False