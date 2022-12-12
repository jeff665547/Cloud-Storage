
n = eval(input())
n = int((n-1)/2)

for i in range(0, n):
    for j in range(0, n-i):
        print(" ", end = "")
    for j in range(0, 2*i+1):
        print("*", end = "")
    print()

for i in range(0, 2*n+1):
    print("*", end ="")
print()

for i in range(n-1, -1, -1):
    for j in range(0, n-i):
        print(" ", end = "")
    for j in range(0, 2*i+1):
        print("*", end = "")
    print()
