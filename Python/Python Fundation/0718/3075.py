lis = []

while True:
    n = eval(input())
    if(n == -1):
        break
    lis.append(n)

print("input =", lis)

AA = lis.copy()
AA.sort()
print("sorted =", AA)
print("max 3rd =", AA[-3])
print("list =",lis)


