n1 = eval(input())
n2 = eval(input())
n3 = eval(input())

if (n1 > n2 and n1 > n3):
    print(n1)
elif(n2 > n3 and n2 > n1):
    print(n2)
elif(n3 > n1 and n3 > n2):
    print(n3)



if (n1 > n2):
    if (n1 > n3):
        print(n1)
    else:
        print(n3)
else:
    if (n2 > n3):
        print(n2)
    else:
        print(n3)
