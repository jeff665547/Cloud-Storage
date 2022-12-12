f = open("../app/stores_old.csv", "r", encoding = "Big5")
#f = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data\\stores_old.csv")
txt = f.readlines()
f.close()

data = []

for i in txt:
    data.append(i.split(","))

n = "Y"

for i in range(1, len(data)):
    if (n == data[i][6]):
        data[i].pop()
        print((",".join(data[i])+ ","))

