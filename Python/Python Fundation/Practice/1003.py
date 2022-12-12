n1 = int(input())
n2 = int(input())
n3 = int(input())

sum = n1 + n2 + n3
average = '%.2f'%(sum/3)
product = n1*n2*n3
if(n1>n2):
    if(n2>n3):
        largest = n1
        smallest = n3
    elif(n1>n3):
        smallest = n2
        largest = n1
    else:
        smallest = n2
        largest = n3
else:
    if(n1>n3):
        largest = n2
        smallest = n3
    elif(n2>n3):
        smallest = n1
        largest = n2
    else:
        smallest = n1
        largest = n3
        
print("sum is", sum)
print("average is", average)
print("product is", product)
print("smallest is", smallest)
print("largest is", largest)
