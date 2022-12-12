
n = eval(input())

def function(n=0): #記得要加預設參數
    AA = 0
    BB = 1
    for i in range(1,n+1):
        AA += i
        BB *= i
    return(AA, BB)
#print(function(n)[1], function(n)[0], sep = "\n")
#ans = function(n)
#print(ans[1], ans[2], sep = "\n")
CC, DD = function(n)
print(CC, DD, sep = "\n")



