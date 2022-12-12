#讀取一個csv檔，並將讀到的csv檔寫到另一個csv檔中
#列出所有門市的門市名稱，並把他放到csv檔裡
#並再把檔案給讀出

f = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data\\stores_old.csv",
          "r", encoding = "big5")
txt = f.readlines()
f.close()

for i in range(len(txt)):
    txt[i] = txt[i].split(",")


    
f5 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data\\stores_new3.csv",
          "w", encoding = "big5")
for i in range(len(txt)):
    #f5.write(",".join(i)) #write的預設裡面並沒有換行符號
    for j in range(len(txt[i])):
        if j == 3 or j ==4:
            f5.write(txt[i][j].strip() + ",") #寫完後用逗號隔開，用+號是因為是字串可以直接用+號去做連結工作的緣故
    f5.write("\n")
f5.close()  


f7 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data\\stores_new3.csv",
          "r", encoding = "big5")
txt5 = f7.readlines()
f7.close()

for i in txt5:
    print(i.strip())


