user={
"id":1,"age":30,"city":"Dhaka"
}
#print(user["id"])
#print(user.get("id"))
print(user.get("name","Unknown"))#get returns values safely,gives none if missing
#checks
print("age" in user)
print("name" not in user)
#view objects
print(user.keys())# return all the keys of your dictionary
print(user.values())#return all the values of your dictionary
print(user.items())# perfect when you need key and value together for looping,transforming data,building ner dicts,comparing and more
print(user)

