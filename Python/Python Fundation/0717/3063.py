AA = []

while True:

    t = eval(input())
    if(t == -1):
        break
    AA.append(t)
    
print(AA)
AA.sort()
print(AA)
AA.insert(3, 10)
print(AA)
print(AA.count(10))
AA.sort()
AA.reverse()
print(AA)
#沒有回傳值的話就不能直接用print印出



