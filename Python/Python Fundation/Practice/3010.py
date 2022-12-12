
n = eval(input())

AA = int(n**(1/2))
count = 0
for i in range(1, AA+1, 1):
    if( n%i == 0 ):
        count += 1

if(count == 1):
    print(n ,"is prime", sep = " ")
else:
    print(n ,"is not prime", sep = " ")

