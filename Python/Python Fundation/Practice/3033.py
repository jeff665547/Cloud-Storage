a1 = eval(input())
d = eval(input())
n = eval(input())

numbers = []
strings = []

for i in range(0, n):
    number = a1 + i*d
    numbers.append(number)
    if(number < 0):
        strings.append("("+str(number)+")")
    else:
        strings.append(str(number))

print(" + ".join(strings), " = " , sum(numbers), sep = "")


