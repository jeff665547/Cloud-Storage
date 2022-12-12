
x = eval(input())

bottle = x
All = x
mod = x

while (All >= 4 ):
    
    handsel = int(All/4)
    mod = All%4
    bottle += handsel
    All = handsel + mod
    if (All == 3):
        All = 4
    
print(bottle)




    