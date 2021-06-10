# Dictionary is nothing but key value pairs
d1={}
# print(type(d1))

d2={"harry":"burger","rohan":"fish","skill":"roti","disha":{"d":"me","f":"you"}}
# this is case sensitive characters hence solve it carefully
d2["kay"]="junk"
d2[233]="dis"
print(d2)
del d2[233]
# print(d2["disha"]["d"])


d3=d2.copy()
del d3["harry"]
print(d2)

print(d2.keys())
print(d2.items())
