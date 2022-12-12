
m = eval(input())

if(m == 1):
    print(m,"is not prime", sep = " ") 
else:
    for i in range(1,m+1,1):
        if(i==1):
            continue
        n = int(i**(1/2))
        count = 0
        for j in range(1, n+1, 1):
            if ( i%j == 0 ):
                count += 1
        if(count == 1):
            print(i,"is prime", sep = " ") 
        