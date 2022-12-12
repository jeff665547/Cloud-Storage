
for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        print(i, "*", j,'=',i*j ,sep ='' ,end ='\t')
    print()    

#格式化輸出


#
n = eval(input())

fct = 0
for i in range(1, n+1):
    if (n%i == 0):
        fct += 1

if(fct==2):
    print(n, "is prime")
else:
    print(n, "is not prime")
    
    


#雙層迴圈簡易版
"*"+"5"
"*" * 5
for i in range(5):
    print('*'*(i+1))

#Break & continue
#無窮迴圈使用技巧
while(True):
    n = input()
    print(n)
    if(n == 'q'):
        break

#continue 是結束本輪(i)的迴圈，直接開始下一次(i+1)的迴圈
n = eval(input())

for i in range(1, n+1, 1):
    if (i == 4):
        continue
    print("floor" ,i, sep = " ")
    


#
Name = input()
Age = int(input())
Gen = input()

print("Name:%s\nAge:%d\nGender:%s"%(Name,Age, Gen))



n = eval(input())
m = eval(input())

for i in range(1, n+1, 1):
    for j in range(1, m+1, 1):
        print("%d*%d=%2d"%(i,j,i*j), end = " ")
    print()    












