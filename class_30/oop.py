# class Employees:
#     def __init__(self,name,no):
#         self.name=name
#         self.no=no
#     def display(self):
#         print(self.name,self.no)
        
# emp1=Employees("mamun","01")
# emp2=Employees("nasim","02")

# emp1.display()
# emp2.display()
# # ===========================================================
# class Dog:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def update_color(self,color):
#         self.color=color
#     def poke(self):
#         print(self.color,self.name,"is smiling")
        
# #=================================================
# d1=Dog("rover","brown")
# d2=Dog("Tommey","White")
# d1.poke()
# # d2.poke()
# d1.update_color("Black")
# d1.poke()

# d2.poke()
# d2.update_color("Red")
# d2.poke()

# # print(d1.__dict__)
# print(dir(d1)) 
# # ======================================

class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
        self.price=0
    def set_price(self,price):
        self.price=price
    
    def get_price(self):
        return self.price
    
    def details(self):
        print("Book Name:",self.name,"\nAuthor Name:",self.author,"\nBook Price:",self.price,"taka")
# ========================================
# b1=Book("opekkha","humayun Ahmed")
# b1.details()
# b1.set_price(255)
# # print(b1.get_price())
# # px=b1.get_price()
# # print(px)
# b1.details()
