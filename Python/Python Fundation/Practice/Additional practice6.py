#讀取stores_old.csv 檔案後
#小練習1:
#請列出公館門市的所有資訊
#小練習2:
#令使用者輸入一門市名稱，並列出該門市的所有資訊
#Combine 1 & 2
old = open("C:/Users/jeff/Desktop/ALL/Python Fundation/0719/Data/stores_old.csv", "r", encoding = "Big5")
file = old.readlines()
old.close()

data = []

for i in file:
    AA = (i.strip()).split(",")
    AA.pop()
    data.append(AA)

name = input()

new = open("C:/Users/jeff/Desktop/ALL/Python Fundation/0719/Data/stores_new5.csv", "w", encoding = "Big5")

for i in data:
    if name == i[3]:
        
        new.writelines(",".join(data[0]) + "\n")
        new.writelines(",".join(i) + "\n")

new.close()


