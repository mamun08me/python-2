class my_calculator:

    def product(self,num1,num2=None,num3=None):
        if num1!=None and num2!=None and num3!=None:
            print(num1*num2*num3)
        elif num1!=None and num2!=None:
            print(num1*num2)
        else:
            print(1*num1)
            
        
# =============================
c1=my_calculator()
c1.product(4,5) 
c1.product(4,5,6)
c1.product(4)