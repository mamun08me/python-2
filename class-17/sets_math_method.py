a={10, 20, 30, 40}
b={30,50,60,70}
print(a.union(b))
print(a|b)#same as union

print(a.intersection(b))#return only shared items
print(a & b)#same as intersection
print(a.difference(b))
print(a-b)
print(b-a)
print(a.symmetric_difference(b))# only non shared items fron both sets
print(a^b)# same as symmetric difference

''' difference between union,intersection amd symmetric difference 
union-all unique items 
intersection- Only shared items
symmetric difference- Only non shared items
difference- in set a but not in set b'''


