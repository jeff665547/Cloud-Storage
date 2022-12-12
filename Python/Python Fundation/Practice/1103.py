
n = eval(input())

AA = dict(zip((0,1,2,3,4,5,6,7,8,9),("","壹","貳","參","肆","伍","陸","柒","捌","玖")))

XX = AA[n%10]

if (int(n/10)%10 == 0):
    BB = (int(n/10)%10)*"拾"
else:
    BB = AA[int(n/10)%10]+"拾"

if (int(n/100)%10 == 0):
    CC = (int(n/100)%10)*"佰"
else:
    CC = AA[int(n/100)%10]+"佰"


if (int(n/1000)%10 == 0):
    DD = (int(n/1000)%10)*"仟"
else:
    DD = AA[int(n/1000)%10]+"仟"


if (int(n/10000)%10 == 0):
    EE = (int(n/10000)%10)*"萬"
else:
    EE = AA[int(n/10000)%10]+"萬"

print(EE+DD+CC+BB+XX+"元整")    