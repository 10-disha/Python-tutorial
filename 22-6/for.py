# exp=[2340,2400,2100,3100,3333]
# total=exp[0]+exp[1]
# total=0
# for item in exp:
#     total=total+item
# print(total)
for i in range(1,11):
    print(i)
exp=[1233,2324,3434,4443]
total=0
for i in range(len(exp)):
    print('month:',(i+1),'expense:',exp[i])
    total=total+exp[i]

print('total expense is:',total)    
