
while(True):
    n = input()
    if ( n.isdigit() == True ):
        break
n = eval(n)
summation = 0

for i in range(1, n+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    summation += factorial

print(summation)


