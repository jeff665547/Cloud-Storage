#讀取stores_old.csv 檔案後，將sid,name,tel,wifi 篩選出來
#並寫入檔案至stores_new.csv 中(要分隔「,」)

file = open("C:/Users/jeff/Desktop/ALL/Python Fundation/0719/Data/stores_old.csv", "r", encoding = "Big5")
store_old = file.readlines()
file.close()

store = []

for i in store_old:
    AA = (i.strip()).split(",")
    AA.pop()
    store.append(AA)

new = []

for i in store:
    row = []
    for j in range(len(i)):
        if j == 0 or j == 3 or j == 5 or j == 6:
            row.append(i[j]) 
    new.append(row)        

newcsv = open("C:/Users/jeff/Desktop/ALL/Python Fundation/0719/Data/stores_new4.csv", "w", encoding = "Big5")

for i in new:
    newcsv.writelines(",".join(i) + "\n")
file.close()


