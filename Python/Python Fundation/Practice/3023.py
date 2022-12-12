
lst = []
lst30up = []
while True:
    n = eval(input())
    if(n == -1):
        break
    else:
        lst.append(n)
    if(n > 30):
        lst30up.append(n)
        
print(lst)
lst.sort()
print(lst)
print(sum(lst30up))