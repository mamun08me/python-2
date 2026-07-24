class Student:

    def __init__ (self,*info):
        if len(info)==3:
            self.name =info[0]
            self.Id =info[1]
            self.CG =info[2]
        elif len(info)==2:
            self.name =info[0]
            self.Id =info[1]
        elif len(info)==1:
            self.name=info[0]
        print("a student object created")
#====================================== 
s1=Student("Carol",1,3.95)
s2=Student("Mamun", 2 , 4)
s3=Student("mamun")
s4=Student()
            