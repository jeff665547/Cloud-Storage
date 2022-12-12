AA = input()

BB = AA.split(",")
CC = []
for i in range(0, len(BB)):
    CC.append(eval(BB[i]))
    
All = sum(CC)

DD = []
EE = []

for i in range(0, len(CC)):
    if(CC[i]%2==0):
        DD.append(CC[i])
    if(CC[i]%2==1):
        EE.append(CC[i])

print(sum(EE))
print(sum(DD))
print(All)