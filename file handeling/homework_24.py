# numbers=[1,2,3,4,5]

# str_list=list(map(lambda i:str(i),numbers))
# print(str_list)


# #Use filter() function to filter even numbers from a list of numbers

# numbers_2=[1,2,3,4,5,6,7,8,9,10]

# even_numbers=list((filter(lambda number:number%2==0,numbers_2)))

# print(even_numbers)

# #Use filter() function to filter strings in a list which length is greater than 10

# string_list=["Mamun or Rashid","siddika","Maisarah","Mahabubar"]

# grater_than_ten_list=list(filter(lambda name:len(name)>=10,string_list))

# print(grater_than_ten_list)

#


    
# namota_list=list(map(lambda number:number,namota_lists))
# print(namota_list)
#Use map() function to create namota of the list [1, 2, 3, 4, 5]

namota_lists=[1,2,3,4,5,6]

def namota(a):
    name=""
    for j in range(1,11):
        name+=str(f"{a}x{j}={a*j}")+"\n"
    return name  
namota_list= list(map(namota,namota_lists))
for i in namota_list:
    print(i)
    print("="*20)
   
==================================================================
namota_lists = [1, 2, 3, 4, 5, 6]

namota_list = list(map(lambda a: [f"{a}x{j}={a*j}" for j in range(1, 11)], namota_lists))

for sub_list in namota_list:
    for line in sub_list:
        print(line)
    print("="*20)
==================================================================
namota_lists = [1, 2, 3, 4, 5, 6]

# ১. ল্যাম্বডা (lambda) ফাংশন এবং ম্যাপ (map) ব্যবহার
namota_list = list(map(lambda a: "".join(f"{a}x{j}={a*j}\n" for j in range(1, 11)), namota_lists))

# ২. নামতা প্রিন্ট করা
for i in namota_list:
    print(i)
    print("="*20)
