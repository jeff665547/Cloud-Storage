atype()#查看物件種類
3**2#次方
//#商數
%#餘數

#input
jeremyLin_height = input("請輸入林書豪的身高:")
type(jeremyLin_height)

#function
def func_name(arg1, arg2,...):
    """
    docstript 的預設位置     就是對此function的描述以及用法放的地方(函數說明文件)
    """
    Ans = arg1 + arg2
    return Ans

#for loop
#list comprehension
#讓for迴圈變得更簡潔
#e.g.
new_list = []
AA = [1,3,5,7,9,11,13,15,17]
BB = [2,4,6,8,10,12,14,16,18]
for i in range(9):
    new_list.append(AA[i] * BB[i])
print(new_list)

another_new_list = [AA[i] * BB[i] for i in range(9)]  ##list comprehension 
print(another_new_list)

#多個iterator (e.g. i, j) 來直接取代向量內的值
#zip函數
zip_list = list()
for i, j in zip(AA, BB):
    zip_list.append(i * j)
print(zip_list)

#map 函數  
#(可簡化 for 迴圈)
#針對某串的iterable(數值，物件)  同時(平行)去運行某一個特定的function 
map(function, iterator)
#e.g.
def square(x):
    return(x**2)
list(map(square, [1, 2, 3]))

#lambda expression
#可用來簡化一些小的運算任務  大型的運算函式還是使用def
list(map(lambda x: x**2, [1, 2, 3]))

#多變數的lambda expression (multiple varaibles)
def max(m, n):
    return m if m > n else n
print(max(10, 3))

max = lambda m, n: m if m > n else n
print(max(10, 3))

#for 也可以對dict去做迴圈 
AA = {"A": 2, "B":3, "C":4, "D":5}
for i in AA.keys():
    print(i)
for j in AA.values():
    print(j)
for i, j in AA.items():
    print(i, j)

#while 迴圈
while condition:
    #do somethings until the condition turns into False

#流程控制
Ans = 36
if (70 == Ans):
    print("correct")
elif (70 > Ans):
    print("smaller")
else:
    print("bigger")

#help
help(type)
?type

#print with format (str.format)
#可利用此方法將數值四捨五入(因為出來是文字 
#所以只需將處裡好的數值轉為小數 或是其他型態的數值)
#e.g. {:.Xf} 有X位數的浮點數
#     {} 文字
BMI = 24.944567
print("Jeremy Lin's BMI is {}.".format(BMI))
print("Jeremy Lin's BMI is {:.2}.".format(BMI))
print("Jeremy Lin's BMI is {:.2f}.".format(BMI))
print("Jeremy Lin's BMI is {:d}.".format(BMI))
#多個輸出  print兩個以上的變數
label = "Normal"
print("Jeremy Lin's BMI is {:.2f}, and his BMI is {}.".format(BMI, label))  #照順序放
print("Jeremy Lin's BMI is {a:.2f}, and his BMI is {b:}.".format(b=label, a=BMI))
print("Jeremy Lin's BMI is {a:.2f}, and his BMI is {b}.".format(b=label, a=BMI))

#判斷式
# ! or not   反轉布林值
# in   在...之中
# !後面可以直接接上shell script的指令 來對電腦的終端機執行命令

not 8 != 7
"J" in "Jeff"

#轉換變數的型別
int()   #將輸入轉換為int  底下依此類推
float()
str()
bool()

print(int(float("8.7")))
bool("False")
bool(0)  #只有丟0才會是false，其餘都是True
bool(100)

#文字的大小順序
#z > y >...> a > Z > Y >...> A

#常用的文字方法  
##跟在物件後面的函數稱為方法(動態 會根據不同的input而得到不同的結果) "string.func(input)"
##而在global enviroment內的函數則稱為函數 "int(string)"
##依賴在物件後方的特性稱為屬性(靜態 單純就是該物件的資訊 不需要傳參數進去因此不會有括號) "AA.attr"
name = "the phantOm oF the opera"
name.title()
name.upper()
name.lower()
name.capitalize()

#去除文字空白的方法
text = "   Alan Walker    "
text.rstrip()
text.lstrip()
text.strip()
text.strip().replace(" ", ",")   #只要.func() 後會回傳值出來就可以一直接其他的function 如本例的程式碼
text.split(" ")

#資料結構
ex = [23, 45, 67, 89, 10, "shit", "Omg", True]
ex[0]
ex[-2]    #倒數第二個值
ex[:3]
ex[0:3]   #從最一開始到第三個
ex[3:]    #從第四個開始到最後
ex[::2]   #step 每兩個取一個值 (公差的概念)

#list and nested list
#放入
extra = [1,2,3,4,5]
ex.append(extra)
ex[len(ex)-1]
ex.insert(1, "insert")   #放在原本index為1的值的前面

#拿出
ex.pop(2)
ex.remove("insert")

#排序
ex.reverse() #不管類型是否相同全部都反著排
AA = ex[3:]
AA.sort()  #同類型的資料做排序(數字:1,2,3,...; 英文: A~Z)
print(AA)

#dict
#dict.get 是將有該index的那個值回傳   若沒有該職責回傳自己設的預設值
AA = {'Name': 'Zara', 'Age': 27}

AA.get('Age', 1)
AA.get('Sex', "NA")

#set
#set 要排序set使用sorted
sorted(name)
#set 只會儲存unique value 重複的資料不會存起來
#set 不支援[] 的index尋找  要取值的話需要先轉換成list在抓出來

#轉換資料結構
tuple()
list()
dict()
set()


#處理資料的重要func
#ndarray:NumPy  模組
#Series:Pandas  模組
#DataFrame:Pandas  模組

#匯入模組(module)
coin = ["head","tail"]

import random
random.sample(coin, 1)

import random as rd   #前兩種都是直接匯入該模組底下全部的函數
rd.sample(coin, 1)

from random import sample   #此種只匯入該模組底下的sample函數  其他函數都不匯入
sample(coin, 1)

import matplotlib.pyplot as plt   # matplotlib.pyplot 大模組底下還有子模組
plt.hist()




##自訂模組 (player.py)
#先建立好一個自訂的function 並且加上對此function的用法描述
#以下的檔案為player.py
def get_favorite_players(x):
    """
    列出你最喜愛的籃球員
    """
    print("Here are my favorite players:")
    for player in x:
        print("- " + player)
#以上的檔案為player.py
#1.將上述檔案存檔(桌面)
#2.打開Anaconda prompt(or command line)
#  Anaconda prompt和command line間的差別差在
#  Anaconda prompt已經收錄了他所涵蓋的應用程式，因此打任何的code他都會認得
#3.cd 到player.py的路徑 (e.g. cd C:\Users\jeff\Desktop)
#4.輸入Jupyter Notebook(可以開python的應用程式)
#5.接著打開一個新的python 3檔案(e.g. New >> Python3)
#  (若已經開啟Jupyter Notebook的話 按一下kernel 內的 Restart即可)
#6.輸入import player後即可使用裡面的function
#7.輸入player.get_favorite_players(["jeff"])
#完成匯入自訂模組


#自訂套件 (多個模組合在一個資料夾)
#多個功能相關的模組可以組織成一個套件
#e.g. 自創statspy套件
#在這個套件中有3個模組
#__init__.py (空白) (一定要存在但不一定要有內容)
#sum.py
#mean.py
#打開cmder並且創立一個新資料夾，此資料夾名稱即為模組名稱 mkdir statspy
#cd statspy
#touch __init__.py
#touch summ.py
#touch mean.py
#code . 利用visual studio code將此資料夾中的檔案打開來做編輯
#__init__.py ==> 空白
#summ.py
def my_sum(x):
    ans = 0
    for i in x:
        ans += i
    return ans

#mean.py
def my_mean(x):
    summation = 0
    cnt = 0
    for i in x:
        cnt += 1
        summation += i
    return summation / cnt
#存檔
#開啟一個新的jupyter notebook (or restart kernel)
#from statspy(套件名稱) import mean(模組名稱)
#from statspy.mean(套件名稱.模組名稱) import my_mean(函式名稱)
#即完成打包套件
#亦可上傳至PyPI -- the Python Package Index (網路位置)來達到網路上的分享
#(若成功上傳到此，則使用者可以直接使用pip install來安裝套件)


#物件導向
#拿類別來產生物件
#Encapsulation(封裝)的意義如下
#物件裡的物件 <=====> 類別的屬性(Attribute)
#物件裡的函數 <=====> 類別的方法(Method)
#由此類別所生出來的object具有自己動態的方法  以及自己靜態的屬性
#和一般自行直接定義出來的object不同

#拿世紀帝國為例:
#Building類 只負責生產人(單位)
class Building():   #類別 使用class來建立 (類別class的名稱需要大寫開頭命名)
    """
    建築物類別
    """
    def __init__(self, name, unit):   #.__init__()初始化方法   #self 為初始化屬性   
    #.__init__() & #self 此兩項為必要的元素  一定要先加入後 後面才可以加入自己想要設定的東西
        self.name = name
        self.unit = unit
        
    def create(self):
        return "{}生產".format(self.name)
town_center = Building("城鎮中心", "村民")
town_center.__doc__
town_center.name
town_center.create()


barrack = Building("軍營", "劍勇")
barrack.name
barrack.create()


#Castle類 除了生產人(單位)外，本身還可以攻擊敵人
class Castle():   #類別 使用class來建立 (類別class的名稱需要大寫開頭命名)
    """
    城堡類別
    """
    def __init__(self, name, unit):   #.__init__()為初始化方法   #self 為初始化屬性   
    #.__init__() & #self 此兩項為必要的元素  一定要先加入後 後面才可以加入自己想要設定的東西
        self.name = name
        self.unit = unit
        
    def create(self):
        return "{}生產".format(self.name)
    
    def attack(self):
        return "{}用弓箭攻擊".format(self.name)
    
castle = Castle("城堡", "特殊兵種")
castle.attack()


#Inheritance(繼承)
class Castle(Building):
    def create(self):
        return "{}生產{}與巨型投石車".format(self.name, self.unit)
    def attack(self):
        return "{}用弓箭攻擊".format(self.name)
    
castle = Castle("城堡", "特殊兵種")
castle.attack()
#上述寫法即為繼承的寫法  它的優點在於直接拿原有的類別來增加方法
#Building為母類別 (相當於 界門綱目科數種 中的 界)，
#Castle為子類別 (相當於 界門綱目科數種 中的 門)
#不但節省coding 空間(節省重複工作)
#更在日後做管理時能便於管理，做更有效率的修改以及更動內容
#(修改方法: 直接重新定義, 修改屬性: 一樣直接重新定義，
#但要記得加上super().母類別的初始化方法(即.__init__(self 不用, ...)))


class Castle(Building):
    def __init__(self, name, unit, siege_unit):
        super().__init__(name, unit)  #有修改需求
        self.siege_unit = siege_unit
        
    def create(self):
        return "{}生產{}與{}".format(self.name, self.unit, self.siege_unit)
    
    def attack(self):
        return "{}用弓箭攻擊".format(self.name)

castle = Castle("城堡", "特殊兵種", "火藥桶")
castle.create()
###############################################################################
#Practice 
#定義一個類別DBFighter
#一個屬性: 姓名
#三個方法: 拳(punch)、踢(kick)、氣功波(shock wave)

class DBFighter():
    def __init__(self, name):
        self.name = name
    def punch(self):
        return("{}使用拳擊!".format(self.name))
    def kick(self):
        return("{}使用踢擊!".format(self.name))
    def shock_wave(self):
        return("{}使用氣功波!".format(self.name))


#定義一個類別Vegta繼承DBFighter, 新增終極光方法(final_flash), 
#利用Vegeta 建立vegeta物件，印出姓名與使用終極閃光方法
class Vegeta(DBFighter):
    def final_flash(self):
        return("{}使用終極閃光!".format(self.name))
    
vegeta = Vegeta("vegeta")
vegeta.final_flash()


#定義一個類別Goku繼承DBFighter, 增加原名(Kakarot)、新增龜派氣功方法(Kamehameha)，
#利用Goku建立goku物件，印出原名與使用龜派氣功方法

class Goku(DBFighter):
    def __init__(self, name, original_name):
        super().__init__(name)
        self.original_name = original_name
        
    def Kamehameha(self):
        return("{}使用龜派氣功!".format(self.original_name))

goku = Goku("goku", "Kakarot")
goku.original_name



##基礎的開發環境(適用於 Unix-like系統: Mac OS, Linux, Windows 需下載cmder)
#基礎命令列指令
#pwd (print working directory 顯示目前的工作路徑(目錄))
#ls (list 把路徑底下的檔案全部顯示出來)
#cd (change directory 切換到其他的工作路徑(目錄) 
#e.g. cd .. 代表回到上一層目錄, cd / 代表回到根目錄(在windows相當於C槽))
#按 control + L 會清空 terminal 的指令 (讓畫面變乾淨)
#mkdir (make directory 新增資料夾)
#touch (建立檔案 e.g. touch bmi.py)
#mv (移動/覆蓋 檔案 e.g. mv )
#cp
#exit (離開)
#應用程式名稱 要開啟的檔案 (利用某應用程式去開啟要開啟的檔案)
#e.g. code . (利用visual studio code 去開啟目前位置裡所有的資料夾以及檔案)
#conda env list (列出目前Anaconda已安裝並且可以使用的虛擬環境)
#conda create -n 虛擬環境的名稱(自行命名) 軟體=版本 (在Anaconda中建立一個虛擬環境)
#e.g. conda create -n python2 python=2


#網路爬蟲
#使用Chrome
#靜態網路擷取(要爬的網站不需要任何的填入選單送出或是登入的動作)
#安裝Chrome外掛: SelectorGadget (Document Object Model, DOM 文件物件模型)
#以IMDb(https://www.imdb.com/title/tt4912910/?ref_=nv_sr_1) 為例
#HTML
#<strong title> 代表粗體
#<span> 代表段落
#安裝Pyquery模組 (在cmd下 pip install pyquery
#or 在jupyter notebook 下 !pip install pyquery 
#因為有驚嘆號(!)會自動直接拉到終端機執行)
from pyquery import PyQuery as pq

movie_url = "https://www.imdb.com/title/tt4912910/?ref_=nv_sr_1"
#1.把網頁的程式碼全部擷取下來
html_doc = pq(movie_url)
print(type(html_doc))
#2.接著將剛剛在SelectorGadget中所得到的下面的文字給複製下來
#  存成一個新的物件
rating_css = "strong span"
#3.使用pyquery中的made方法並且把它給print出來
print(html_doc(rating_css))
#4.接著把左右的標籤給去掉
print(html_doc(rating_css).text())
#5.裡面的資料已經是string了可以直接取用
type(html_doc(rating_css).text())
rating = float(html_doc(rating_css).text())
##若擷取下來的資料中有多個資訊(但並非每個都是自己想要的)時
#請不要直接取text()方法
#用迴圈把資料給過濾掉
#e.g.擷取上映日期
genre_css = ".subtext a"
print(html_doc(genre_css))  #有多個資訊
print(html_doc(genre_css).text())  #有多個資訊  但只有上映日期是我們想要的
#用迴圈處理
genre = []   #用genre去收集
len(html_doc(genre_css)) #html_doc(genre_css)可以看長度(len)
for g in html_doc(genre_css):
    print(g.text)   #這邊的text是屬性  之前的text都是方法
    genre.append(g.text.lstrip().replace("\n",""))   #為了得到tidy data (乾淨的data)  
    #所以做了一些進一步的處理  e.g. 去空白還有"\n"
print(genre)
genre[3]

#打包成一個函數
def get_movie_info(movie_url):
    """
    Get movie information give movie URL
    """
    #css selector 的位置
    rating_css = "strong span"
    genre_css =  ".subtext a"
    cast_css = ".primary_photo+ td a"
    genre = []
    
    html_doc = pq(movie_url)
    rating = float(html_doc(rating_css).text())
    genre_release = html_doc(genre_css)
    genre_release_len = len(genre_release)
    for i in range(genre_release_len):
        if i < (genre_release_len - 1):
            genre.append(genre_release[i].text.lstrip().replace("\n", ""))
        else: 
            release_date = genre_release[i].text.replace("\n", "")
    cast = [c.text.lstrip().replace("\n", "") for c in html_doc(cast_css)]  
    #list comprehension
    
    #如果有多個回傳值，且又要給其他使用者使用的話，
    #不建議使用tuple來回傳，建議用dict來做會較好(因有索引值)
    info_dict = {
            "Rating": rating, 
            "Genre": genre,
            "Release Date": release_date,
            "Cast": cast
            }
    return info_dict
    
mi = get_movie_info("https://www.imdb.com/title/tt4912910/?ref_=nv_sr_1")    

infinity_war = get_movie_info("https://www.imdb.com/title/tt4154756/?ref_=nv_sr_2")

print(mi["Release Date"])

print(infinity_war["Rating"])

print(mi["Cast"][0])

#上述已完成單一網站頁面的資料擷取

#下面開始進行從IMDb的網站首頁打入關鍵字一直到跳到我們想要的網頁頁面
#首先產生出搜尋目標的url
#(觀察在不同的搜尋項目下，最後出來的網站網址之間的差別在哪
#把不同的地方挖掉即可)
from urllib.parse import quote_plus
from pyquery import PyQuery as pq

def get_movie_url(movie_title):
    """
    Get movie URL from a movie title
    """
    domain_name = "https://www.imdb.com"
    movie_title_encoded = quote_plus(movie_title)  #產生搜尋目標的url
    query_url = "https://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=all".format(movie_title_encoded) 
    #產生網址
    first_search_css = ".odd:nth-child(1) .result_text a" 
    #使用selectorgadget來找出第一個搜尋選項的css位置
    
    html_doc = pq(query_url)
    movie_url = domain_name + html_doc(first_search_css).attr("href")
    #利用html_doc().attr("href") (網頁物件.attr("參數")) 
    #來擷取第一個最相關結果的網頁連結 ("href")就是網頁連結所放的參數位置
    
    return movie_url

get_movie_url("Avengers: Infinity war")
get_movie_url("Mission: Impossible - Fallout")

#上述已完成從IMDb的網站首頁打入關鍵字一直到跳到我們想要的網頁頁面(某個電影的電影資訊)

#下面開始進行前兩個function的整併
#意即直接輸入電影名稱後就馬上得到電影相關資訊
def imdb_movie_crawler(movie_titles):
    """
    Get movie info given movie title
    """
    movie_info_dict = dict()
    for movie_title in movie_titles:
        movie_url = get_movie_url(movie_title)
        movie_info = get_movie_info(movie_url)
        movie_info_dict[movie_title] = movie_info
    return movie_info_dict

imdb_movies = imdb_movie_crawler(["Mission: Impossible - Fallout", 
                                  "Avengers: Infinity war"])

imdb_movies["Mission: Impossible - Fallout"]

imdb_movies["Avengers: Infinity war"]["Genre"][0]



#動態網路擷取(資料擷取的過程需要透過按鈕點選or表單填寫...等  和網路做互動)
#(需要使用到terminal or cmd)
#0.建立一個虛擬環境
#  (Why 虛擬環境? -- 寫虛擬環境可以告訴系統接下來的程式碼是需要在
#   甚麼樣的環境中才能運行，若今天是幫公司開發一個產品時，就會大量利用此技術
#   將所需的基本軟體(e.g. python)給導入後，再執行後續相關的程式。如此一來，
#   才不會有過了好幾年以後因為一些基本軟體的更新進而導致程式碼無法運作的問題
#   發生。
#1.打開Anaconda prompt(cmd)
##常用的conda指令
# conda env list  (查看目前電腦有哪些虛擬環境)
# conda create -n selenium python=3  (建立一個名稱為 selenium 的Python3虛擬環境)
# (conda remove --name selenium --all  (移除一個名稱為 selenium 的虛擬環境)    要移除時才用此指令)
# conda activate selenium  (啟動一個名稱為selenium的虛擬環境)
# (conda deactivate  (停止一個虛擬環境)    要離開時才用此指令)
# pip install 套件or模組名稱  e.g.pip install numpy pandas selenium ipykernel
# (安裝需要的模組)
# python -m ipykernel install --user --name selenium --display-name "selenium"
# (在此虛擬環境下做Jupyter Notebook的Kernel設定 (連結 Jupyter Notebook 與虛擬環境))
# jupyter kernelspec remove selenium (在此虛擬環境下移除Jupyter Notebook的Kernel設定)
# conda deactivative
#完成建立虛擬環境
#
#2. 更新chrome 瀏覽器(一定要到最新版)
#3. 下載驅動 Chrome 瀏覽器的 Driver  並且解壓縮至想要的地方(e.g. 桌面)
#   (https://sites.google.com/a/chromium.org/chromedriver/downloads)
#
#4. 打開jupyter notebook (目前沒試過其他的IDE)
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path="C:/Users/jeff/Desktop/chromedriver.exe")
#   #(在這之中C:/Users/jeff/Desktop/chromedriver.exe為剛剛第3步解壓縮後的檔案放置位置)
#   #(Mac OS 的話不需要打副檔名.exe)
#注意: 此時若跳出一個chrome程式並且顯示chrome目前受到其他軟體所控制  則代表成功
#5. 此時已經可以由python程式碼來操控chrome瀏覽器
#driver.get("https://www.python.org")    #這邊的driver是因4命名了driver變數
#driver.get("https://www.nytimes.com")   
#(上面的兩行code代表叫chrome先到第一個python的網站 接著再前往NY times的網站)
#driver.back()  (叫chrome回上一頁)
#driver.forward()  (叫chrome到下一頁)
#driver.close()  (關閉chrome瀏覽器程式)
#
#
#接下來的範例和靜態網頁擷取的目標結果相同    但概念上以及動作切入點不相同
#動態網頁擷取的概念像是一個實體的機器人 親自到電腦前面去操作使用電腦的感覺
#我們必須要跟這台電腦講他下個動作要怎麼做  鼠標要移到哪裡  移到了之後要按
#左鍵或是填寫資料之類的  然而靜態的網頁擷取則是直接透過更動網址(網址要自己生)
#來到達想到的網站頁面再擷取裡面的資訊
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/jeff/Desktop/chromedriver.exe")
imdb_url = "https://www.imdb.com"
driver.get(imdb_url)   #到IMDb網站

navbar_query_css = "#navbar-query"     #(搜尋欄的CSS位置)
navbar_query_elem = driver.find_element_by_css_selector(navbar_query_css)    #(告訴系統到搜尋欄的那個位置)
navbar_query_elem.send_keys("Mission: Impossible - Fallout")    #(告訴系統在那個位置輸入值"Mission: Impossible - Fallout")
#(如果是告訴系統在那個位置清空文字輸入框則是navbar_query_elem.clear())

submit_css = "#navbar-submit-button .navbarSprite"    #(搜尋圖示(放大鏡圖示)的CSS位置)
submit_elem = driver.find_element_by_css_selector(submit_css)     #(告訴系統到放大鏡圖示的那個位置)
submit_elem.click()    #(告訴系統點擊那個按鈕(連結))

first_result_css = ".odd:nth-child(1) a"   #(搜尋結果中的第一個結果的CSS位置)
first_result_elem = driver.find_element_by_css_selector(first_result_css)   #(告訴系統到第一個結果的那個位置)
first_result_elem.click()    #(告訴系統點擊那個連結)

rating_elem = driver.find_element_by_css_selector("strong span")   #(告訴系統到評價的CSS位置)
rating = float(rating_elem.text)     #(利用.text屬性把值給取出來)
print(rating)

genre_release_date_elem = driver.find_elements_by_css_selector(".subtext a")   #(告訴系統到含有上映日期的CSS大略位置  
# 注意這邊是find_elements_by  因為該位置有多個值，如果只有單一一個的話element就沒有s)
genre_release_date_len = len(genre_release_date_elem)
genre = []
for i in range(genre_release_date_len):
    if i < (genre_release_date_len - 1):
        genre.append(genre_release_date_elem[i].text)  #(利用.text屬性把值給取出來)
    else:
        release_date = genre_release_date_elem[i].text
        
print(genre)
print(release_date)

cast_elem = driver.find_elements_by_css_selector(".primary_photo + td a")     #(告訴系統到含有演員陣容的CSS位置
cast = [c.text for c in cast_elem]
print(cast)

#接著將上述所做的事情function化
def get_movie_info(movie_title):
    """
    Get movie information given a movie title.
    """
    driver = webdriver.Chrome(executable_path="C:/Users/jeff/Desktop/chromedriver.exe")
    imdb_url = "https://www.imdb.com"
    driver.get(imdb_url)   #到IMDb網站

    navbar_query_css = "#navbar-query"     #(搜尋欄的CSS位置)
    navbar_query_elem = driver.find_element_by_css_selector(navbar_query_css)    #(告訴系統到搜尋欄的那個位置)
    navbar_query_elem.send_keys(movie_title)    #(告訴系統在那個位置填上movie_title的值)

    submit_css = "#navbar-submit-button .navbarSprite"    #(搜尋圖示(放大鏡圖示)的CSS位置)
    submit_elem = driver.find_element_by_css_selector(submit_css)     #(告訴系統到放大鏡圖示的那個位置)
    submit_elem.click()    #(告訴系統按下那個按鈕(連結))

    first_result_css = ".odd:nth-child(1) a"   #(搜尋結果中的第一個結果的CSS位置)
    first_result_elem = driver.find_element_by_css_selector(first_result_css)   #(告訴系統到第一個結果的那個位置)
    first_result_elem.click()    #(告訴系統按下那個連結)

    rating_elem = driver.find_element_by_css_selector("strong span")   #(告訴系統到評價的CSS位置)
    rating = float(rating_elem.text)     #(利用.text屬性把值給取出來)

    genre_release_date_elem = driver.find_elements_by_css_selector(".subtext a")   #(告訴系統到含有上映日期的CSS大略位置  
    # 注意這邊是find_elements_by  因為該位置有多個值，如果只有單一一個的話element就沒有s)
    genre_release_date_len = len(genre_release_date_elem)
    genre = []
    for i in range(genre_release_date_len):
        if i < (genre_release_date_len - 1):
            genre.append(genre_release_date_elem[i].text)  #(利用.text屬性把值給取出來)
        else:
            release_date = genre_release_date_elem[i].text
        
    cast_elem = driver.find_elements_by_css_selector(".primary_photo + td a")     #(告訴系統到含有演員陣容的CSS位置
    cast = [c.text for c in cast_elem]
    
    movie_info = {
        "Rating": rating,
        "Genre": genre,
        "Release Date": release_date,
        "Cast":cast
    }
    driver.close()      #(截取完資料後 將瀏覽器給關閉)
    return movie_info

#導入亂數以及時間模組
import random
import time

movie_titles = ["Mission: Impossible - Fallout", "Avengers: Infinity War", "La La Land"]

movie_info = dict()
for movie_title in movie_titles:
    movie_info[movie_title] = get_movie_info(movie_title)
    time.sleep(random.randint(2, 7))  
    #(重要: 加入亂數時間讓系統在每次迴圈做完時休息一下  避免被官網認出是機器人
    #因為如此的高頻率搜尋的動作會造成對方網路維護上的麻煩以及困擾)

movie_info["La La Land"]["Cast"][0]
movie_info["La La Land"]["Cast"][1]

#上述即完成動態網頁資訊擷取


#############################################################################
#以下為練習(Yahoo! 奇摩股市：上市單日成交價排行)
#1. 前往 Yahoo! 奇摩股市
#2. 點選更多排行
#3. 點選上市行情類排行榜：單日成交價排行
#4. 點選列出前一百名排行
#5. 將股票代號/名稱擷取下來

from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/jeff/Desktop/chromedriver.exe")
stock_url = "https://tw.stock.yahoo.com/"
driver.get(stock_url)

more_css = ".yui-text-left .yui-text-left table tr:nth-child(1) .stext div a"
more_elem = driver.find_element_by_css_selector(more_css)
more_elem.click()

dayrank_css = "br+ .yui-text-left tr:nth-child(5) a"
dayrank_elem = driver.find_element_by_css_selector(dayrank_css)
dayrank_elem.click()

first100_css = "table+ p a+ a"
first100_elem = driver.find_element_by_css_selector(first100_css)
first100_elem.click()

stock_name_css = ".name a"
stock_name_elem = driver.find_elements_by_css_selector(stock_name_css)

stock_price_css = ".name+ td"
stock_price_elem = driver.find_elements_by_css_selector(stock_price_css)

ticker_name = [tk.text for tk in stock_name_elem]
price = [float(p.text) for p in stock_price_elem]

driver.close()
print(ticker_name)
print(price)

#把有KY的公司和沒有KY的公司給分開來
#有KY的公司: 代表該公司雖然在台灣掛牌上市，但其公司註冊地並不在台灣
#python code原生寫法
ky_prices = []
ky_tickername = []
nonky_prices = []
nonky_tickername = []
for i in range(len(ticker_name)):
    if "KY" in ticker_name[i]:
        ky_prices.append(price[i])
        ky_tickername.append(ticker_name[i])
    else:
        nonky_prices.append(price[i])
        nonky_tickername.append(ticker_name[i])
nonky_prices
nonky_tickername

#pandas寫法
import pandas as pd

df = pd.DataFrame()
df["ticker_name"] = ticker_name
df["price"] = price
ky = df[df["ticker_name"].str.contains("KY")]
nonky = df[~df["ticker_name"].str.contains("KY")]  #用~來反轉True/False
nonky


#將公司代號以及公司名稱分開
#python code原生寫法
ticker = []
company = []
for t in ticker_name:
    ticker.append(t.split()[0])
    company.append(t.split()[1])
print(ticker)
print(company)

#pandas寫法
df["ticker_name"].str.split()






