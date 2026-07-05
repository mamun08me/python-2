# 1. Create a python program to write down prime numbers from 1 to 1000 in a file called prime-numbers.txt
# 2. Create a python program to write 1 to 30 namota (counting table) in a file called namota.txt 

# with open("prime-numbers.txt", "w") as f:
#     for i in range(2, 1001):
#         is_prime = True
        
#         for j in range(2, int(i**0.5) + 1): 
#             if i % j == 0:
#                 is_prime = False 
#                 break
                
#         if is_prime:
#             print(i) # স্ক্রিনে দেখাবে
#             f.write(str(i) + "\n") # ফাইলে লিখবে এবং নতুন লাইনে যাবে (\n)

with open("namota.txt", "w") as f:
    for i in range(1,31):
        for j in range(1,11):
            namota= f"{i}x{j}= {i*j}\n"
            print(namota)
            f.write(str(namota))
        f.write(str("="*10)+"\n")
            
    