
n = eval(input())
folder = []

for i in range(n,0,-1):
    folder.append(i)
    print("data" ,i)
print()
for i in range(0,n):
    AA = folder.pop()
    print("data", AA)

