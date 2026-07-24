class Student:

    def __init__ (self,**info):
        if len(info)==3:
            self.name =info["name"]
            self.Id =info["Id"]
            self.CG =info["CG"]
        elif len(info)==2:
           self.name =info["name"]
           self.Id =info["id"]
        elif len(info)==1:
            self.name =info["name"]
        print("a student object created")
#====================================== 
s1=Student(name="Carol",Id=1,CG=3.95)
s2=Student(name="Mamun", Id=2 , CG=4)
s3=Student(name="mamun")
s4=Student()