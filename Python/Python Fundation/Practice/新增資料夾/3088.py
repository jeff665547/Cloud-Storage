#f = open("../app/stores_old.csv", "r", encoding = "big5")
f = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data\\stores_old.csv")
txt = f.readlines()
f.close()

txt[5]

data = []

for i in txt:
    data.append(i.split(","))
    
n = input()

for i in range(0, len(data)):
    if (n == data[i][3]):
        print(",".join(data[i]))
