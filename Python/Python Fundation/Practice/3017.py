
add = 0
count = 0
maxi = 0
while(True):
    
    n = eval(input())
    
    if( n == -1 ):
        break
    else:
        add += n
        count += 1
        average = '%.1f'%(add/count)
        if( maxi <= n ):
            maxi = n
            pos = count
        
print(add, average, maxi, pos, sep = "\n")

