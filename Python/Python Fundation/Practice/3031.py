n1 = int(input())

dozen = int(n1/12)
mod = n1%12

if(mod == 0):
    print(dozen, "dozen", sep = " ")
else:
    print(dozen, "dozen", "and", mod, sep = " ")
