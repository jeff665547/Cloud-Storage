import random

Ans = random.randint(2,99)

count = 0
Min = 1
Max = 100
print("1 < ? < 100")
while (True):
    n = eval(input())

    if( Min < n < Max ):
        
        if(n > Ans):
            count += 1
            if(Max > n):
                Max = n
            print("wrong answer, guess smaller")
            print("已猜次數:", count, "次", sep = " ")
            print(Min,"< ? <",Max)
            continue
            
        elif(n == Ans):
            count += 1
            print("bingo answer is", n)
            print("總共次數:", count, "次", sep = " ")
            break
            
        else:
            count += 1
            if(Min < n):
                Min = n
            print("wrong answer, guess larger")
            print("已猜次數:", count, "次", sep = " ")
            print(Min,"< ? <",Max)
            continue
    else:
        count += 1
        print("out of range")
        continue
    
    