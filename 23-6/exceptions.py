x=input("enter num1:")
y=input("enter num2:")
try:
    z=x/int(y)
except ZeroDivisionError as e:
    print('divsion by zero exception')
    z=None
except Exception as e:
    print('type is:',type(e).__name__)
    z=None    
print("division is:",z)        