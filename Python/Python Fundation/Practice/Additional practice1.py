n = eval(input())
m = eval(input())

def f1(n, m):
    print("f1() n*m =", n*m)

f1(n, m)

def f2(n, m):
    n*m
    return(n*m)

ans = f2(n, m)

print("f2() n*m =", ans)
print("f2相乘的結果=", ans)
print("f2() + 50 =", ans+50)
