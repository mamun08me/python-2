# with open("name.txt", "r") as file:
#     content=file.read()
#     print(content)
    
# with open("name.txt", "w") as file:
#     # file.write("hello world\n")
#     # file.write(" i am writing a file\n")
#     file.write("this is for testing.....")


      
# with open("name.txt", "a") as file:
#     file.write("\nhello world\n")
#     file.write(" i am writing a file\n")
#     file.write("this is for testing.....")  
    
# lines=["\nI love python\n","\nI am new in python\n"]

# with open("name.txt", "a") as file:
#     file.writelines(lines)

import os
import pathlib
if os.path.exists('name.txt'):
    print("file exists")
else:
    print("file not exists")
print('='*45)
    
file_path=pathlib.Path('name.txt')
if file_path.exists():
    print('file exists')
    
print('='*45)   
print(os.path.abspath('name.txt'))
print(os.path.getsize('name.txt'))

with open('name.txt','r') as file:
    print(file.read(5))
    
file1 = open("file3.txt", "w")
file1.write("Mamun""\namar sonar bangla\n")
file1.close()
    
    
    