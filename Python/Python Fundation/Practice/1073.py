
All = input()

All = All.split(" ")
All.pop()

#file = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/data.txt", "w", encoding = "big5")
file = open("../app/data.txt", "w", encoding = "big5")
file.write(" ".join(All))
file.close()

#data = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/data.txt", "r", encoding = "big5")
data = open("../app/data.txt", "r", encoding = "big5")
Data = data.readlines()
data.close()


print(Data[0] + " ")