iA = {"蘋果", "香蕉", "鳳梨", "芭樂"}
iB = {"鳳梨", "蘋果", "水梨", "蓮霧"}

iA.add(input())
iA.add(input())
iB.add(input())
iB.add(input())

print("刪除了", iA.pop())
print("刪除了", iB.pop())
iA.remove('蘋果')
iB.remove("蓮霧")

inter = iA.intersection(iB)
union = iA.union(iB)
ans = union - inter

#print(inter)
#print(union)
#print(ans)

ansls = list(ans)
ansls.sort()
print(ansls)

print(iA-iB)
print(iB-iA)
print(union-inter)


#函數與資料結



ls = [99,88,77]
sorted(ls)
ls.sort()
ls
sorted((99,88,77)) #把TUPLE丟進去 但只會回傳list

#function
def hi():
    for i in range(3):
        print("Hi", i+1)

hi()

n = eval(input())
def hi(n):
    for i in range(n):
        print("Hi", i+1)
hi(n)
   
    
n = eval(input())
m = eval(input())

def multiply1(n, m):
    print(n*m) #print是沒有回傳值的
multiply1(n, m)
multiply1(n, m)+1


def multiply2(n, m):
    return(n*m)
multiply2(n, m)  #此為有回傳值，相當於在此介面打上multiply2(n, m)的結果，因此要另外把它給存下來，再把它給print出來
multiply2(n, m)+1 



    
    
