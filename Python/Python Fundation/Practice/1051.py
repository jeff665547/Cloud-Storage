
m = eval(input())
n = eval(input())

Class = []

for i in range(0, m):
    grades = input()
    grades = grades.split(" ")
    classmate = []
    for j in range(0, n):
        classmate.append(eval(grades[j]))
    Class.append(classmate)

Allsum = []
Allnum = []
for i in range(0, m):
    print("class", i+1)
    Sum = sum(Class[i])
    n = len(Class[i])
    Avg = Sum/n
    Allsum.append(Sum)
    Allnum.append(n)
    for j in range(0, n):
        print(" ", j+1 , ": ", Class[i][j], sep = "")
    print(" sum:", Sum)
    print(" avg: %.2f" %(Avg))

Allsum = sum(Allsum)
print("total: ", Allsum, ", avg: %.2f" %(Allsum/sum(Allnum)), sep = "")


