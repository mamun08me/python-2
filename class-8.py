import random
n= random.randint(1,100)
chance_left=3

while chance_left !=0:
    x=int(input("enter a random number between 1-100: "))
    if x<n:
        print(" number is too low")
    elif x>n:
        print("Number is too high")
    else:
        print("congratulations.you got it right")
        break
    chance_left=chance_left-1
    
print("the number was: ",n)
print("chance left: ", chance_left)
    

