'''#Dict comprehensions
3 components
--key value expressions
--a loop 
---optional conditions'''
#challenge : keep only string values & convert them to UPPPERCASE
user={"id":10,"name":"Mamun","age":30, "city":"Dhaka"}
user_string={
    k: v.upper()#expressions
    for k, v in user.items()#loop
    if isinstance(v,str)#filter
}
print(user_string)