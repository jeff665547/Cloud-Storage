
n = eval(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        print("*" , sep = "", end = " ")
    if (i == n):
        print(sep = "", end = "")
    else:
        print()
    
        