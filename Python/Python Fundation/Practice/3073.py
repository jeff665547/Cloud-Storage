n = eval(input())

def twofunction(n = 1):
    factorial = 1
    summation = 0
    for i in range(0, n):
        factorial *= (i+1)
        summation += (i+1)
    return(summation, factorial)

print(twofunction(n)[1], twofunction(n)[0], sep = "\n")

