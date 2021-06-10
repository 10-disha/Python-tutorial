# list data structure

grocery=["harpic","vim","bhindi",34]
print(grocery[0])

numbers=[1,2,33,334,5]
# numbers.sort()
# numbers.reverse()
# if u are taking negative slicing take -1  not lower than that
print(numbers[1:5:2]) 
print(numbers)
# append adds number at the last of the list
numbers.append(33)
print(numbers)

# rather insert can add number at any place of your choice
numbers.insert(2,44)
numbers.remove(2)

# pop will remove the last number
numbers.pop()
print(numbers)

# mutable = can be changed
# immutable= cannot be changed

# tuple is immutable and list is mutable

tp=(1,)
print(tp)

a=1
b=8
a,b = b,a
print(a,b)