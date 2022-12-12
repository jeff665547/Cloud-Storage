#讀取一個csv檔，並將讀到的csv檔寫到另一個csv檔中
#列出所有門市的門市名稱，並把他放到csv檔裡

f = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data\\stores_old.csv",
          "r", encoding = "big5")
txt = f.readlines()
f.close()

for i in range(len(txt)):
    txt[i] = txt[i].split(",")

for i in range(len(txt)):
    print(txt[i][3], end = '\n')
    #print(txt[i][4])
    
f5 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data\\stores_new2.csv",
          "w", encoding = "big5")
for i in txt:
    f5.write(",".join(i)) #write的預設裡面並沒有換行符號
f5.close()  

