
AA = []

while (True):
    n = eval(input())
    AA.append(n)
    if(n == -1):
        break

BB = AA.copy()
print(BB.sort())
print(BB.insert(3, 10))
print(BB.count(10))
print(BB.reverse())


