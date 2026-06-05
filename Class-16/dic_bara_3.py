user={
"id":1,"age":30,"city":"Dhaka"
}
#looping
for u in user:
    print(u,user[u])
    
for key, value in user.items():
    print(f"{key}:{value}") # it is more convinient to use
    