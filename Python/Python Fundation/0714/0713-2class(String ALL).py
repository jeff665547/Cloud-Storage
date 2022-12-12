#抓出個位數有3
n = input()
n%10 == 3
#抓出十位數有3


#顯示各種進位的表示方式
print(bin(23097351))#二進位
print(oct(23097351))#八進位
print(hex(23097351))#十六進位

print(0b1011000000111000000000111) #開頭0b代表此數值為二進位制
print(0o130070007) #開頭0o代表此數值為八進位制
print(0x1607007)  #開頭0x代表此數值為十六進位制

#格式化輸出
# %d & %f  整數與浮點數
'這是整數%d印完了' %(10)
'這是%d整數%d印完了' %(10, 20) #d為整數的意思  以10進位顯示，在這邊沿用C語言的decimal

'這是%d整數%f印完了' %(10, 20.5) #f為float 以10進位顯示


import math
print("PI = %f"%(math.pi))
print("PI = %8.4f"%(math.pi))  #%8.4f 為顯示出小數點後4位  8為8個字(8個空格)，並且將預設的字靠右對齊(小數點也是1格)
                               #要空格數 >字數此指令才會有效
print("PI = %-8.4f"%(math.pi))


'這是%d整數%.1f印完了' %(10, 20.5) #f為float 以10進位顯示
'這是%d整數%7.2f印完了' %(10, 20.5) #f為float 以10進位顯示
'這是%d整數%3.2f印完了' %(10, 20.5) #f為float 以10進位顯示
'這是%d整數%-9.2f印完了' %(10, 20.5) #f為float 以10進位顯示  "-"為靠左對齊  預設為靠右對齊
'這是%d整數%09.2f印完了' %(10, 20.5) #f為float 以10進位顯示   0的意思則是將"前方"有空位置的地方補上0(注意:只能補0, 不能補其他數字)
'這是%d整數%-9.2f印完了' %(10, 20.5) #f為float 以10進位顯示  "-"為靠左對齊  預設為靠右對齊

#字串(%s)

'這是%s整數%3.2f印完了' %("apple", 20.5) #f為float 以10進位顯示  "-"為靠左對齊  預設為靠右對齊
'這是%.2s整數%3.2f印完了' %("apple", 20.5) #s為string .3為只取前3個字元做輸出
'這是%.3s整數%3.2f印完了' %("apple", 20.5) #s為string .3為只取前3個字元做輸出
'這是%7.3s整數%3.2f印完了' %("apple", 20.5) #s為string ".3"為只取前3個字元做輸出  7和上面的float一樣為總空格數
'這是%4.7s整數%3.2f印完了' %("apple", 20.5) #s為string   4無效和float時一樣

#顯示出原本長的模樣 %r 、repr()

n1 = 132
n2 = "123"
n1
n2
print(n1)
print(n2)  #print會把引號拿掉
print(repr(n1))
print(repr(n2))
print("%r"%(n2))
print(True)
print(repr(True))

test = "%r %r %r"
print(test%(1,2,3))
print(test%("dad", "mom", "son"))
print(test%(True, False, "Neither"))
print(repr(0), repr("1"))

#格式化  for only python 3   將格式化變成一種自訂function
#比較無法自訂顯示格式

a = "{}+{}={}"
print(a)
print(a.format(7,9,7+9))

b = "{city}, {country}"
print(b)
print(b.format(city = "Taipei", country = "Taiwan"))

c = "{1} + {2} = {0}"
print(c)
print(c.format(3+4, 3, 4))

#字典形式
print("會員編號:%(#)08d"%{"#":123456})
money = 888888888888888888881111987.98
print("$%*.2f"%(7, money))    #用*來代替7，統一在後方輸入

#若使用的是字典形式，則前面function中需列出字典的索引值(需是字串形式，因為索引值是放在前面要顯示的字串中，所以已經加了""，變成字串的形式，因此在後者字典中索引值也要便成字串形式才行)
name = {"game":"xbox", "apple":"iphone", "camera":"nikon"} 
print("%(apple)s, %(camera)s, %(game)s" %(name)) 
print("會員編號1:%d, 會員編號2: %d"%(10, 20))
print("會員編號2:%(#2)d, 會員標號1:%(#1)d"%{"#1":10, "#2":20})
print("會員編號1:%(num1)d, 會員編號2:%(num2)d" %{"num1":10, "num2":20})
print("會員編號1:%(1)d, 會員標號2:%(2)d"%{"1":10, "2":20})
print("會員編號1:%(1)d, 會員標號2:%(2)d"%{1:10, 2:20})

#型態轉換
str1 = "64"
print(int(str1)) #將字串改成十進位的數值
print(int(str1, 8)) #改成8進位
print(int(str1, 16)) #改成16進位
eval(input()) #eval會自動判斷出型態並且自動轉成該型態

"Hello" + str(2) #將數值轉成字串後，可以做字串的加法(結合)

#字串可用索引值去取出字串內的內容或插入部分資料(但不可以修改內容，只能組合)，具有順序性

"""
三個引號
=跨行字串
=多行註解
"""

str[0:len(str):1] #從第0個開始印印到最後一個, str為字串變數名稱

toast = "PYTHONSLICE"
len(toast)
toast[-1]
toast[-2]
toast[-5]
toast[-5:] #沒寫結束就是預設-最後一個結束
toast[:6]  #沒寫結束就是預設-第零個開始
toast[:6] + toast[-5:]
"PYTHONSLICE"[:6] == toast[:6]
toast[0:len(toast):1]

#list + 索引值
st = [1,2,3,4,5,6,7,8,9,"apple"]
st[5:]
st[::]
st[::-1]
st[::1]
st[::2]
st[-1:0:-2] #從-1開始一直到第0格，每2格往回數顯示
st[-1:0:-1]

s = "Hello. World"
print(s)
print(s[2:])
print(s[0:7] + "The Beautiful" + s[6:12]) #有使用:者，a:b 則代表是要取a開始到b-1的位置停止的數，第b位置的文字不會被挑出
s[-1:0:-2]
s[::-2] == "drW.le"


#Tuple 元組;組件(from China)
toast = "PYTHONSLICE"
tuples = toast[0:3], toast[3:6], toast[6:9], toast[9:11]  #由文字所組成的tuple
tuples
tuples[0]
tuples[0:3]
tuples[2][0]
tuples[2][1:3]

a = 1,2,3  #不用加任何的括號，這樣的資料型態就是tuple，其特徵就是執行完後最外面包的就是小括號
a

("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
 "Friday", "Saturday")[3]

#Dictionary 字典
days = {"1":"Sunday", "2":"Monday", "3":"Tuesday", 
        "4":"Wednesday", 5:"Thursday", "num6":"Friday", 
        "7":"Saturday"}

days["2"]
days[3],days[4]
days[5]
days["num6"]

#若為數值型態，無法直接將想要的數值取出，需先轉成string再取出數值，再變回數值
a = 12345
a[2]

eval(str(a)[2])

#字串轉換
n = "    Apple  Banana  cccc  of in"
n.strip() #將string 字串變數裡的()內的東西給刪除，沒寫就是預設刪空白
n.strip(" A")
n.swapcase() #將大小寫互換
n.lstrip()  #將string 字串變數裡左邊的東西給刪除()內放要刪除的東西，若字串左邊有空白記得前面要加一個空白
n.lstrip("A")
n.lstrip(" Aa") #無法刪掉a因為需先將a前面的字串都先刪除
n.lstrip(" Ap")
n.lstrip(" Apl")

n.capitalize() #句首第一個自首字母大寫
n.title() #把句子用標題(title)的大小寫方式給呈現出來
n.upper() #全部小寫
n.lower() #全部大寫
AA = n.title()
BB = n.upper()
CC = n.lower()
n.zfill(96)  #把字串前方補0直到字串長度等於96
n.istitle()  #判斷字串是否符合title的型態(不管前面的幾個空白)
AA.istitle()
BB.isupper() #判斷字串是否全部大寫(不管前面的幾個空白)
CC.islower() #判斷字串是否全部小寫(不管前面的幾個空白)
DD = "  APPLE BANANA"
DD.isupper()

AA = "xbox.gif,iphone.jpg"
AA.endswith(".jpg")  #判斷字串內是否有以()內的東西結尾， 後面可以再加入想探討的字串範圍
AA.endswith(".gif")
AA.endswith(".gif", 0,7) #搜尋範圍的結尾要多加一個索引值去搜尋
AA.endswith(".gif", 0,8) 
AA.startswith("xbox") #判斷字串內是否有以()內的東西做開頭， 後面可以再加入想探討的字串範圍
AA.startswith("iphone", 9,14) #搜尋範圍的結尾要多加一個索引值去搜尋
AA.startswith("iphone", 9,15)
AA.startswith("iphone", 9,119)

BB = """
apple123
banana456
"""

CC = "appLE123"

DD = "   appLE123"

EE = "Apple,"
FF = "Apple"

AA.isalnum()  #判斷變數裡的內容是否是a~z  A~Z  0~9的字元 (標點符號 空白  換行  一率不接受)
BB.isalnum()
CC.isalnum()
DD.isalnum()
EE.isalnum()
FF.isalnum()

FF.isalpha()  #判斷變數裡的內容是否全部都只是英文字母(不分大小寫)

AA = "11 22 33 44 55 66 77 88 99 110"
BB = "112233445566778899110"
CC = "     "

AA.isdigit() #判斷字串內是否只有數字
BB.isdigit() 

AA.isspace() #判斷字串內是否只有空白
CC.isspace()

#抽換字串裡的某些字元 (一次可以替換多個字元)
intab = "aeiou"  #欲取代的字元
outtab = "12345"  #新取代字元
trantab = str.maketrans(intab, outtab)  #形成mapping關係  str.maketrans(from, to) 

sentence = "this is string example...wow!!!"  #原字串及句子，欲取代的字串及句子
sentence.translate(trantab)  #由上面自訂的mapping換字元

#字串常用函式
AA = "This is NTU CSIE class during NTU summer in NTU nearby NTU MRT station."
BB = """ABCD
EFG
IJK
"""
CC = "A\nb  \nccccccc\rdd\ra"   #\r是回車就是將標點移到最前面的行首,皆在後面打得字元會直接覆蓋上去   \n是換行  通常用的Enter是兩個加起來
print(CC)
DD = "C:\\|D:\\|E:\\|G:\\|F:\\|I:\\"
EE = " Czngrxtulxtizns, yzu hxve pxssed the czmpetitizn. "

AA.split(sep = " ")  #以sep分割成子字串，回傳儲存子字串的list
AA.split(sep = " ", maxsplit = 1) #maxsplit為"子"字串最多的數量，為分割幾次。 
AA.split(sep = " ", maxsplit = -1)
AA.split(sep = " ", maxsplit = 0)

AA.splitlines(True) #以"\n"和"\r"作為分割的區隔字元 
BB.splitlines()
BB.splitlines(True) #True 就是連同一些分類依據("\n" or "\r")也留下來
CC.splitlines()
CC.splitlines(True)

DD.partition("|")  #可以先把資料用("|")內的符號切成兩半，形成3個元素組成的tuple(第一部分, 字串中第一個()內的分割符號 , 第二部分資料)
AA.partition(" ")  #分割符號變成是第一個空白

AA.count("i") #計算某一個特定字元或字串在目標中出現了幾次，後面可以再加入計數的範圍(index)
AA.count("NTU")
AA.count("NTU",8,33)
AA.count("NTU",8)

AA.find("NTU") #尋找NTU的位置(index)，後面可以再加入搜尋的範圍(index)  若回傳值為-1，則代表要找的字元(串)不在其中
AA.find("NTU",8,33)
AA.find("NTU",8,9)

AA.index("NTU") #和上面函式的功能雷同，但當回傳值是ValueError時，則代表要找的字元(串)不在其中，不會回傳-1，要用Error的處理方式
AA.index("NTU",9,33)
AA.index("NTU",9)

EE.replace("z", "o").replace("x", "a") #先將字串中z字元替換成o字元,再將x字元替換成a字元
EE.replace("z", "o", 2)  #將字串中z字元替換成o字元，並且只換2次，第3次出現的z就不再替換
EE.replace("Czngrxtulxtizns" , "Congratulations")

#.join與split
AA = ["I", "love", "NTU"] #先建立一個list

BB = " ".join(AA) #使用.join把字串用" "符號將()裡list的內的多個字串給串起來，並且形成一個新的單一字串
CC = ",".join(AA)

BB.split(" ")   #split與join相反
CC.split(",")

#Application for .join and split
"this is a set".split()

for s in "this is a set".split():
    s = s.capitalize()
    print(s)

" ".join([s.capitalize() for s in "this is a set".split()])

n = [45, 22, 89, 6, 23, 77, 90, 42]
[i for i in n if i > 30]


