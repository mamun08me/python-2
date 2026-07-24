#class inheritance
class persion:
    def __init__(self,name,age,salary):
        self.name=name#public
        self._age=age#protected
        self.__salary=salary#private
        #getter method
        def get_salary(self):
        return self.__salary
p1=persion("abdullah",27,30000)
p1.name

class Employee(person):
    def__init__(self,name,agr) 