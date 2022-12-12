
f = open("../app/stores_old.csv", "r", encoding = "Big5")
#f = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data/stores_old.csv", "r", encoding = "Big5")
file = f.readlines()
f.close()

newfile = []

for i in file:
    line = i.replace("\n", "")
    if (line.split(",")[3] == "公館門市"):
        print(line)


