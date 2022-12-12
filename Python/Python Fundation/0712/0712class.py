for i in [11,22,33]:
    print("i å€¼ =", i)

print(range(10))
list(range(10))
list(range(3, 15 ,4))
list(range())
for i in range(10):  #range(10)=0~9 å…±10å€‹æ•¸
    print("i å€¼ =", i)

sum1 = 0
for i in range(101):
    sum1 += i
else:
    print(" å°‡1 åˆ°100 åŠ ç¸½ï¼Œæ‰€å¾—ç¸½å’Œç‚º", sum1) 
 
    
n = eval(input())

AA = 0
for i in range(1, n):
    AA += i
    print(i, end='+')
else:
    AA += n
    print(i+1,"=",AA)



n = eval(input())

AA = 0
for i in range(1, n+1):
    AA += i
    print(i, end='')
    if ( i != n ):
        print("+", end = "")
    else:
        pass
else:
    print(" =",AA)
    

n1 = eval(input())
n2 = eval(input())
compute = input()

if(compute == "+"):
    Ans = n1 + n2
elif(compute == "-"):
    Ans = n1 - n2
elif(compute == "*"):
    Ans = n1 * n2
elif(compute == "/"):
    Ans = n1 / n2

Ans = "%.2f"%(Ans)
print("%.2f"%(n1), compute, "%.2f"%(n2), "=" , Ans)



#while的優勢:不知使用次數時(使用者輸入迴圈次數)

n = 0
total = 0
ct = -1
MaxVal = 0
MaxPOS = 0
while (n != -1):
    ct += 1
    total += n
    if (n>MaxVal):
        MaxVal = n
        MaxPOS = ct
    n = eval(input())


print(total)
print(total /ct)
print(MaxVal)
print(MaxPOS)
  
a = [2,55,7,78,89]
max(a)
sum(a)
len(a)
sum(a)/len(a)


#巢狀迴圈(雙重迴圈) 
#(a)
n = eval(input())

for i in range(0,n): # row = 5
    for k in range(0,i+1): #column = 8
        print("*", end = "")
    print()


#(b)
n = eval(input())

for i in range(n,0,-1): # row = 5
    for j in range(0,i): #column = 8
        print("*", end ="")
    print()

#(c)
n = eval(input())
sum = 1

for i in range(0,n): # row = 5
    for k in range(0,i+1): #column = 8
        print(sum, end = " ")
        sum += 1
    print()

#exercise
n = eval(input())

for i in range(0,n): # row = 5
    for k in range(0,i+1): #column = 8
        print(" ", end = " ")
    for k in range(i+1, n): #column = 8
        print("*", end = " ")
    print()


