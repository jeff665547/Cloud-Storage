
n = eval(input())

for i in range(0, n-1):
    print(" ", end ="")
print("*")

for k in range(0, n-2):    
    for i in range(k, k+3):
        for j in range(0, n-i-1):
            print(" ", end = "")
        for j in range(0, 2*i+1):
            print("^", end = "")
        print()

m = n-2
for i in range(m):
    for j in range(int((n+1)/2)):
        print(" ", end = "")
    for j in range(m):
        print("#", end = "")
    print()



