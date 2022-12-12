N = eval(input())
money = input()
Nremove = eval(input())
pos = input()

moneyarray = []
money = money.split(" ")
for i in range(0, (N//100 + 1)):
    moneyrow = []
    if( i != N//100 ):
        for j in range(0, 100):
            moneyrow.append(eval(money[i*100 + j]))
    else:
        for j in range(0, (N%100)):
            moneyrow.append(eval(money[i*100 + j]))
    moneyarray.append(moneyrow)

posarray = []
pos = pos.split(" ")
for i in range(0, (Nremove//100 + 1)):
    posrow = []
    if( i != Nremove//100 ):
        for j in range(0, 100):
            posrow.append(eval(pos[i*100 + j]))
    else:
        for j in range(0, (Nremove%100)):
            posrow.append(eval(pos[i*100 + j]))
    for k in posrow:
        if( k == 0 ):
            continue
        else:
            moneyarray[(k-1)//100].pop((k-1)%100)
            moneyarray[(k-1)//100].insert((k-1)%100, 0)
    posarray.append(posrow)
     
Max = []
Sum = 0
for i in range(0, (N//100 + 1)):
    Sum += sum(moneyarray[i])
    rowmax = max(moneyarray[i])
    Max.append(rowmax)

allmax = max(Max)
rowpos = Max.index(allmax)
colpos = moneyarray[rowpos].index(allmax)
finalpos = rowpos*100 + colpos + 1

print(Sum)
print(finalpos, allmax)



''' wrong
N = eval(input())
Nmoney = []
money = input()
money = money.split(" ")

for i in money:
    Nmoney.append(eval(i))

lost = eval(input())

pos = input()
pos = pos.split(" ")
position = []

for i in pos:
    position.append(eval(i))

for i in position: 
    Nmoney.pop(i-1)
    Nmoney.insert(i-1, 0)

print(sum(Nmoney))
print(Nmoney.index(max(Nmoney)) + 1, max(Nmoney))

'''