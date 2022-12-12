n = input()
Alldata = []

if (n == "0.txt"):
    f0 = open("../app/0.txt", "r", encoding = "UTF-8")
    #f0 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/0.txt", "r", encoding = "UTF-8")
    data0 = f0.readlines()
    f0.close()
    Alldata.append(data0)
elif(n == "1.txt"):
    f1 = open("../app/1.txt", "r", encoding = "UTF-8")
    #f1 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/1.txt", "r", encoding = "UTF-8")
    data1 = f1.readlines()
    f1.close()
    Alldata.append(data1)
elif(n == "2.txt"):
    f2 = open("../app/2.txt", "r", encoding = "UTF-8")
    #f2 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/2.txt", "r", encoding = "UTF-8")
    data2 = f2.readlines()
    f2.close()
    Alldata.append(data2)
elif(n == "3.txt"):
    f3 = open("../app/3.txt", "r", encoding = "UTF-8")
    #f3 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/3.txt", "r", encoding = "UTF-8")
    data3 = f3.readlines()
    f3.close()
    Alldata.append(data3)

New = []
for i in Alldata:
    for j in i:
        j = j.strip()
        New.append(j)
        
money = []
name = []
for i in range(len(New)):
    if (i%2 == 0):
        name.append(New[i])
        print("chef", New[i], end = " ")
    else:
        print(New[i])
        money.append(eval(New[i]))
    if (i == len(New)-1):
        print("Total:", sum(money))
        print("Avg: %.2f" %(sum(money)/(len(New)/2)))




