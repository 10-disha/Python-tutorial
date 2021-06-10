s=set()
# print(type(s))
# s_from_list = set([1,2,3,4])
# print(s_from_list)
# print(type(s_from_list))
s.add(1)

# set retains only unique values different from list
s.add(2)
s1=s.union({1,2,3})

# also we can do s.intersection,s.remove,s.disjoint 
# min, max,type,len  
print(s,s1)