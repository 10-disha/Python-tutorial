# create a list check if it is a number than greater than 6 or not

items=[int,float,2,3,33,4,4,55,66,7]

for item in items:
    if str(item).isnumeric() and item>6:
        print(item)