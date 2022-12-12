
n = eval(input())
m = eval(input())

for i in range(1, n+1, 1):
    for j in range(1, m+1, 1):
        print("%d*%d=%2d"%(i,j,i*j), end = " ")
    print()
    
