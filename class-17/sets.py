my_set={10, 30, 20,10}
print(my_set)
#print(my_set[1])#set is not indexed
my_set.remove(30)#mutable
print(my_set)

a={10,20,30,40}
a.add(50)
print(a)
#a.update("mamun")
#a.update({1,2})
#a.update([1,2])
a|={1,2}
print(a)
#a.remove(100)
a.discard(100)
#a.pop()
#a.pop()
print(a)


#set is unordered beacuse it uses hash table 
#set is not allowed duplicates or unique
#set is not indexed
#set is mutable

#difference among list,tuple and set

#list[]------ordered, Duplicate, indexed Mutable 
#tuple()-----ordered, Duplicate, indexed, Not Mutable
#Set{}-------only mutable
#index-based methods do not work with sets
#add() method uses to insert a item somewhere in the set,but only if it is new
#update() method use for merging another group of values(iterable)into set
#we can use math operators as quick shortcuts:|&-^
#|= for update shortcuts

#if you remove missing values which is not in sets there will be error showing instead you can use discard
#discard use for removing the item if it is exists and does nothing if it does not