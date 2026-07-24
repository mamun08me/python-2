from multipledispatch import dispatch

class my_calculator:
    @dispatch(int)
    def product(self,a):
        print(a)
    
    @dispatch(int,int)
    def product(self,a,b):
        print(a*b)
    @dispatch(int,int,int)   
    def product(self,a,b,c):
            print(a*b*c)
        
        
# ========================================
c1=my_calculator()
c1.product(4,5) 
c1.product(4,5,6)
c1.product(4)
# c1.product(4,5,6,7,8)