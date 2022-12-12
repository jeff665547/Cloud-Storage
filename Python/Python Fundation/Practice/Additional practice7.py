#讀取stores_old.csv 檔案後 列出所有有wifi的門市的所有資訊

old = open("C:/Users/jeff/Desktop/ALL/Python Fundation/0719/stores_old.csv", "r", encoding = "Big5")
file = old.readlines()
old.close()

data = []

for i in file:
    AA = (i.strip()).split(",")
    AA.pop()
    data.append(AA)
    
new = open("C:/Users/jeff/Desktop/ALL/Python Fundation/0719/Data/stores_new6.csv", "w", encoding = "Big5")
new.writelines(",".join(data[0]) + "\n")

for i in data:
    if(i[6] == "Y"):
        new.writelines(",".join(i) + "\n")

new.close()

