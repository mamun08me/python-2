'''i = 1
while i <= 10:
    n = i
    while n <= i*10:
        print(f"{n}x{i}={n*i}")
        n += i
    i += 1
    print()
    
    
i = 1
while i <= 10:
    j = 1  # এই কাউন্টারটি প্রতিবার ১ থেকে শুরু হবে (১, ২, ৩...১০)
    while j <= 10:
        print(f"{i}x{j}={i*j}")
        j += 1  # j এর মান ১ করে বাড়বে
    i += 1
    print()  # নামতা শেষে লাইন ব্রেক'''
    
row=int(input("enter the number of rows: "))
i=1
while i<=row:
    j=1
    while j<=i:
        print("*", end=())
        j+=1
    print()
i+=1

        
        
    
