

def f(n=0): #記得要加預設參數
    BB = 1
    for i in range(1,n+1):
        BB *= i
    return(BB)

n = eval(input())
m = eval(input())

print(int(f(n)/f(n-m)))
