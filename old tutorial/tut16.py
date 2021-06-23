list1=[["harry",1],["carry",2],["marry",4],["farry",3]]


dict1=dict(list1)
print(dict1)
for item,lollipop in list1:
    print(item,lollipop)

for item,lollipop in dict1.items():
    print(item,lollipop)

for item in dict1:
    print(item)