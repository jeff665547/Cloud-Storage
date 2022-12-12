
n = eval(input())

AA = dict(zip((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19),("","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven","twelve", "thirteen", "foutreen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")))
BB = dict(zip((0,11,12,13,14,15,16,17,18,19),("","eleven","twelve", "thirteen", "foutreen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")))
CC = dict(zip((0,10,20,30,40,50,60,70,80,90),("","ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety")))

if(0 < n < 10000000):
    if (n == 1):
        D ="dollar"
    else:
        D = "dollars"
    
    if((n%100)>19):
        AAA = CC[int((n%100)/10)*10] + " " + AA[n%10] + " "
    else:
        AAA = AA[n%100] + " "
        
    if(int(n/100)%10 != 0):
        H = AA[int(n/100)%10] + " " + "hundred "
    else:
        H = ""
    
    if ((int(n/1000)%1000 == 0)):
        T =""
    else:
        T ="thousand "
    
    if((int(n/1000)%100)>19):
        T_AAA = CC[int((int(n/1000)%100)/10)*10] + " " + AA[int(n/1000)%10] + " "
    elif((int(n/1000)%100) != 0):
        T_AAA = AA[int(n/1000)%100] + " "
    else:
        T_AAA = ""
        
    if(int(n/100000)%10 != 0):
        T_H = AA[int(n/100000)%10] + " " + "hundred "
    else:
        T_H = ""
    
    if ((int(n/1000000)%1000 == 0)):
        M =""
    else:
        M ="million "
    
    if((int(n/1000000)%100)>19):
        M_AAA = CC[int((int(n/1000000)%100)/10)*10] + " " + AA[int(n/1000000)%10] + " "
    elif((int(n/1000000)%100) != 0):
        M_AAA = AA[int(n/1000000)%100] + " "
    else:
        M_AAA = ""
        
    if(int(n/100000000)%10 != 0):
        M_H = AA[int(n/100000000)%10] + " " + "hundred "
    else:
        M_H = ""
    
    print(M_H + M_AAA + M + T_H + T_AAA + T + H + AAA + D)

else:
    
    if (n >= 10000000):
        print("n > 9999999")
    elif (n < 1):
        print("n < 1")
    print("system error")
