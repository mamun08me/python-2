app_name = "Smart Utility Function Toolkit"

x="abc"
def show_app_scope():
    """গ্লোবাল স্কোপ প্রদর্শনের জন্য ফাংশন"""
    print(f"--- Global Scope Example ---")
    print(f"Application Name (Accessed from Global Scope): {app_name}")
    print(f"-----------------------------------------\n")
    global x
    x="name"
show_app_scope()    
print(x)


product_lambda=lambda x, y, z: x*y*z
def product(x,y,z):
    return x*y*z
print(product(12,10,10))

print(product_lambda(12,10,10))

to_uppercase_lambda = lambda s: s.upper()

def to_uppercase(s):
    return s.upper()

print(to_uppercase('mamun'))
print(to_uppercase_lambda('mamun or rashid'))

string_lwngth=lambda s: len(s)
def string_length(s):
    return len(s)

print(string_length("mamun"))
print(string_lwngth("mamun"))


is_greater_lambda=lambda x, y: x > y
def is_greater(x, y):
    return x > y

print(is_greater(50,60))
print(is_greater_lambda(50,60))

positive_lambda=lambda x: x if x > 0 else 0
def positive_or_zero(x):
    return x if x > 0 else 0
print(positive_or_zero(-5))
print(positive_lambda(-5))

Even_or_odd_lambda=lambda x: "Even" if x % 2 == 0 else "Odd"
def even_or_odd(x):
    return "Even" if x % 2 == 0 else "Odd"
print(even_or_odd(5))
print(Even_or_odd_lambda(5))


cube_lambda=lambda x: x ** 3
def cube(x):
    return x ** 3
print(cube(5))
print(cube_lambda(5))

power_lambda=lambda x, y: x ** y
def power(x, y):
    return x ** y
print(power