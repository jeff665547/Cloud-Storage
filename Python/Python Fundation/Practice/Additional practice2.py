#讀取一個csv檔，並將讀到的csv檔寫到另一個csv檔中

f = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data\\stores_old.csv",
          "r", encoding = "big5")
txt = f.readlines()
f.close()

f5 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data\\stores_new1.csv",
          "w", encoding = "big5")
for i in txt:
    f5.write(i.strip() + "\n") #write的預設裡面並沒有換行符號
f5.close()  


  