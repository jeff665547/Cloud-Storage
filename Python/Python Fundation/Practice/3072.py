
def factorial(n = 0):
    fact = 1
    for i in range(1, n):
        fact *= (i + 1)
    return(fact)

factorial(3)

def C(n, m):
    Ans = factorial(n)//(factorial(m)*factorial(n-m))
    return(Ans)

n = eval(input())
m = eval(input())
print(C(n, m))

