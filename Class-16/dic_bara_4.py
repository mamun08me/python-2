user={
"id":1,"age":30,"city":"Dhaka"
}
#add,Remove,Update
user["name"]="Mamun"#add
user["age"]=35#update
user.update({"age":40,"city":"Rangpur"})#update method
print(user)
#age=user.pop("age")
#age=user.pop("Salary","not found")
#print(user)
#print("Removed item:",age)
#pop() removes a key from the dictionary and returns its value

#user.pop() # error will occur if left blank, should pass the argument
user.popitem()
user.popitem()
print(user)

