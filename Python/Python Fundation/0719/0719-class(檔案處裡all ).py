#檔案處理
#做檔案讀取的3大步驟:開檔 => 讀寫檔 => 存檔(關閉檔案)
#access_mode其預設是讀取模式"r"  主要分為兩大類，第一大類是文字檔讀寫模式，第二大類是二進位檔的讀寫模式(網路爬蟲比較常會用到)

#開檔(再開下一個檔案之前一定要先把上一個檔案給關起來，不要重疊)
#必須把此執行檔存到和資料同一個路徑底下(#此在spyder底下無法執行，要直接用IDLE去執行)
#先寫三步驟
#f1 = open("text.txt", "r")  #相對路徑的一種寫法(因為都在同一個資料夾底下，所以這樣寫即可)，"r"就是代表 access mode，access mode分成兩種模式，一種是文字檔的讀寫模式，另一種則是二進位檔(e.g.轉換成二進位的影像、聲音、文字)的讀寫模式(網路爬蟲的時候比較有可能會用到)
f1 = open("C:/Users/jeff/Desktop/ALL/Python Fundation/0719/Data/text.txt", "r")
#open(file_name, [,access_mode][buffering]), 其中buffering代表要給這筆資料多少的記憶體暫存空間，可忽略不寫
txt1 = f1.readlines() #一次讀多行，但需要記憶體夠的前提下才能使用，讀出來的檔案以list的形式存在
f1.close()

txt1[0] #第一列 
txt1[1] #第二列
txt1[2] #第三列
txt1[3] #第四列

for i in txt1:
    print(i.strip())  #去掉每一行頭尾的空白與換行

#相對路徑表示法(程式檔與所要呼叫的資料檔案的相對關係)(優點:程式移到哪都可以被執行，缺點:相對關係不能被破壞)
f1 = open("./Data/text.txt", "r") #"./" 代表與此執行檔同樣的資料夾底下的部分(表示接續同一層目錄下) "./" 可以不用打 
f1 = open("../0719/Data/text.txt", "r") #"../" 代表在此執行檔的上一層目錄

#絕對路徑表示法(完整的打出路徑名稱)(缺點:程式移到哪都要在改過路徑之後才能被執行)
f1 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data/text.txt", "r") #因為\加上其他字母會有特殊的意義，所以才需要用到/或是\\，但不要混合使用

txt1 = f1.readlines() #一次讀多行
f1.close()
#讀取檔案
f2 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data/sim.txt",
          "r", encoding = "gb2312") 
#因檔案為簡體中文形式，所以要先將編碼形式在open的時候改成是舊時代的簡體編碼gb2312(or gbk or gb18030)才能看的到
txt2 = f2.readlines() 
f2.close()
for i in txt2:
    #print(i)
    print(i.strip())


#CSV (comma-seperated values) #用逗號分隔開來的檔案
#在windows中預設就是直接把檔案存成是Big5 編碼形式(開啟檔案的預設編碼也是Big5)，所以如果存成編碼為UTF-8的形式，在windows打開會變成亂碼
#所以在windows的excel中必須從"資料"那裏匯入，再到裡面改編碼形式改成UTF-8才可以閱覽，才不會變成是亂碼
f3 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data/stores_old.csv",
          "r", encoding = "big5") 
#建議為了維持程式的相容性，encoding要把它給寫出來
txt3 = f3.readlines()
f3.close()
for i in txt3:
    print(i.strip())

#寫入功能 write() 也可以作為轉換編碼形式的功能
lst = ["apple", "banana", "pineapple", "pen"]  #寫入list, 先把要寫的東西給寫好

f0 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data/write01.txt",
          "w", encoding = "utf-8")  #注意"w" write模式中如果在資料夾中已經有該檔案了(已經存在)，在執行一次這一個程式就會把原有的檔案給覆蓋掉，注意:如果不要覆蓋掉，只是想要追加資料的話請用"a" 附加模式(不會把原有檔案蓋掉),"w"和"a"這兩個模式相同的地方是萬一這個檔案先前沒有人建立起來的話，系統會幫使用者建立好新的檔案。
f0.write("這是第一行\n") #需要自己加入換行("\n")的指令，否則會全部連在一起，write沒有換行的功能
f0.write("這是第二行\n")
#f0.writelines(lst)  #放進的這一個list必須全部內容都是字串，不可以有其他的內容，執行了之後會發現全部黏在一起，想要分割就用write + join的語法
f0.write(" ".join(lst))  #將"".join 加入     ""內放要插在list中每一個元素之間作為分隔的東西e.g. " "(以空白做間隔)), "\n" , ","(以逗號做間隔), "\t"(tab)
f0.close() #一定要加入這一行，否則資料只會停留在暫存區，不會寫到檔案內(系統會等全部要寫入的東西都寫完之後再全部一起寫入到檔案裏頭，但在這行程式以前，資料只會停留在記憶體的某個空間(暫存區))


f4 = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\0719/Data/write01.txt",
          "r", encoding = "utf-8") 
txt4 = f4.readlines()
f4.close()
for i in txt4:
    print(i.strip())

#more practice in additional practice 4
#Additional Practice 4
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



