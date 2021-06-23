# with the use of function

def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total

tom_exp_list=[231,333,4,44]
joe_exp_list=[234,55,66,66]

toms_total=calculate_total(tom_exp_list)
joes_total=calculate_total(joe_exp_list)

print("tom's total:",toms_total)
print("joes total:",joes_total)





