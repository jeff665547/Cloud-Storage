
lst = []

while (True):
    n = eval(input())
    if (n == -1):
        break
    else:
        lst.append(n)

def sor(lst):
    lst1 = lst.copy()
    lst1.sort()
    return(lst1[-3], lst1)

print("input =", lst)
print("sorted =", sor(lst)[1])
print("max 3rd =", sor(lst)[0])
print("list =", lst)