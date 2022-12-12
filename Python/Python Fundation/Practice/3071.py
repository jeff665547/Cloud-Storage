def factorial(n = 0):
    fact = 1
    for i in range(1, n):
        fact *= (i + 1)
    return(fact)

factorial(3)

def P(n, m):
    Ans = factorial(n)//factorial(n-m)
    return(Ans)

n = eval(input())
m = eval(input())
print(P(n, m))
