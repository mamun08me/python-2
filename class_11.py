a=float(input("enter first number: "))
b=float(input("enter second number: "))
c=float(input("enter third number: "))

if a>b:
    if a>c: 
        print(f" the largest number is : {a}")
    else:
        print(f" the largest number is : {c}")
    
else:
    if b>c:
        print(f" the largest number is : {b}")
    else:
        print(f" the largest number is : {c}")
    