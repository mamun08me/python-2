# a=[1,2,3,4,5,6,7,8,9,10]
# # result=[]

# # for i in a:
# #     if i%2==0:
# #         result.append(i)
# # print(result)

# # #list comprehension
# # new_resutlt=[i for i in a if i%2==0]
# # print(new_resutlt)
# a_new=[i**2 if i%2==0 else i for i in a]
# print(a_new)

b=[-10,1,2,3,4,-16,-15]

i=0
while i<len(b):
    if b[i]<0:
        b[i]=0
    i+=1
print(b)


nums=list(range(0,11))

result={i: "even" if i%2==0 else "odd"  for i in nums}
print(result)