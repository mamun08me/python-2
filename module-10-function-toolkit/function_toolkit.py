
app_name = "Smart Utility Function Toolkit"

def show_app_scope():
    print(f"--- Global Scope Example ---")
    print(f"Application Name (Accessed from Global Scope): {app_name}")
    print(f"------------------------------------------------------------------------------------\n")
show_app_scope()
    

# 📌 Step 3: Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

# 📌 Step 2: Program Introduction
print("=========================================")
print(f"Welcome to {app_name}")
print("=========================================\n")



# 📌 Step 4: User Input Menu
while True:
    print("--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5.Exit")
    
    choice = input("Select an option (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = add(num1, num2)
                print(f"result:Summation of  {num1} and {num2} are = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: Subtraction of  {num1} and {num2} are= {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: multiplication of  {num1} and {num2} are = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result:Division of  {num1} by {num2} is {result}")
            elif choice==5:
                print("Exiting...")
                
    else:
        print("\n=======================================")
        break


# 📌 Step 6: Lambda Practice
print("--- Lambda Practice: Square a Number ---")
square = lambda x: x ** 2

user_num = float(input("Enter a number to square: "))
print(f"The square of {user_num} is: {square(user_num)}")

print("-----------------------------------------\n")


# 📌 Step 7: Map Function Usage
print("--- Map Function Practice ---")
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original List: {numbers_list}")

squired_list = list(map(lambda x: x * 2, numbers_list))
print(f"Multiplied by 2 (Using map function): {squired_list}\n")


# 📌 Step 8: Filter Function Usage
print("--- Filter Function Practice ---")
even_list = list(filter(lambda x: x % 2 == 0, numbers_list))
print(f"Even Numbers (Using filter): {even_list}")
print("==============================================")