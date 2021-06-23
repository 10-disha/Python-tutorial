# string slicing
# index starts with 0


mystr = "harry is a good boy"
print(len(mystr))
# this will skip alternate will get print
print(mystr[::2])
# 3rd colun will skip characters
# negative indices start from reverse 

print(type(mystr))
print(mystr.isalnum())
# isalnum comes false as there are spaces in between string

print(mystr.endswith("bo"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.upper())
print(mystr.replace("is","are"))