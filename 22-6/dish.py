indian=["samosa","daal","naan"]
chinese=["role","fried rice"]

dish=input("enter a dish name:")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
else:
    print("unknown")        