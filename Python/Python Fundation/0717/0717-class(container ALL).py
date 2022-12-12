#有回傳值的函數可做3件事: 1.存下來 2.印出來 3.打點繼續做其他操作(其他function)
type() #判斷是甚麼類型的容器以及資料

#容器
#Tuple 序對 (其存取速度較list快，有順序性，但不可更改內容，增加，刪除，因為儲存在記憶體是已連續的形式存在，而非片段，因此讀取和存取速度較快)
#2 method (尋找以及計數)
t = ("a", "b", "join", "a", "mary", "a", "b")
t.index("a", 1,5)
t.count("mary")
t.count("b", 0, 5)  # tuple 裡的count 沒有辦法接收三個值

#list  串列 (可更改、增加、刪除內容，可放任意資料型態，有順序性)
#創建一個空的list
a = []
b = [1,2,3,"3",[4],(5)]
print(b[1])
print(b[3])
print(repr(b[3]))
print(b)

st1 = [] #空list
st1 = list()
st1

#加東西、直接更改東西(list 專屬語法
#       .append一律加在最後面, 但一次只能加一個物件  
#       .extend後面加可以拆開的資料型態ex: 字串、容器
#       .insert 可指定要加在哪一個位置    
#        += 就是extend  
#       [] = 加索引值直接給定欲更改的值 )
st1.append(123)
st1.append([1,2,3])
st1.append("apple")
st1.append(1,2,3,4) #一次只能加一個物件，這邊已經有4個物件了，需要用一個容器把它給包起來，然後再用extend
st1.extend([11,22])
st1
st1.extend("good")
st1
st1.insert(1, 11) #(加入的位置， 加入的值)
st1.insert(100, 10) #若指定位置不存在，則自動加入最後面
st1

a  = [1, "a", 6]

a += [5.4]  # += 和.extend 的效果是相同的 注意要用list的型態去包裝
a += ["123"]
a[2] = 7  #list變更索引值為2內容的方法



#刪東西(.remove 依照資料內容刪東西, ()內放要刪除的資料內容   刪第一個符合()內的元素
#       .pop 依照索引值刪除東西
#       .clean 全部清空)
st1.remove(11) 
st1
st1.pop() #預設為刪除最後一個值
st1.pop(2) #刪除索引值為2的值，並且回傳已刪除的元素
st1.pop(-1) #刪除最後一個值
st1.clear #全部清空


#尋找值、計數
st1.index("apple") #只接受有序性的容器 e.g.string, tuple, list
st1.index([1,2,3]) 
st1.index(22, 2, 8) #(尋找的值，起始範圍，終止範圍)
st1.count("o") #這裡的count 不能加入搜尋範圍


#排列、比大小 (在值是可以比較的情況之下，全部都是數值or字串)
st1 = [345, 231, 6, 2, 7, 84, 6532]
st2 = ["aCC", "AAA", "ABB", "AAB" , "ACC"]
st3 = ["30", "100", "70"]

st1.sort()  #由小排到大，要由大排到小，請再加上reverse()的幫忙
st2.sort()  #按照字母順序，大寫編碼較小，小寫編碼較大
st3.sort()  #數值字串比大小 是使用字串的方式去比較, 先比較第一個字的大小，一樣的話再依序往後比
st1.reverse() #將排列順序顛倒

#複製 .copy
s3 = st1.copy()  #複製一份到新的記憶體
s2 = st1 #此為共用空間，而非複製
s2 is st1 #若為True則代表共用同一個物件(共用空間) s2做更動，st1也會做更動
s2 == st1 #看值是否相等

#尋找元件在記憶體中的 id  (儲存空間)
AA = [1,2,3,"apple"]
AA[0] = 99
BB = [1,2,3]
CC = [246, BB]
AA.append(CC)
print(id(AA))  #印出來的結果就是指AA在記憶體的空間位置
print(id(BB))
print(id(CC))
print(id(AA[4])) == print(id(CC))
print(id(AA[4][1])) == print(id(BB))
print(id(CC[1])) == print(id(BB))


#字典 dict (dictionary)
#{"Key":"Value", "Key":"Value", .....}
#四種表達字典的方式
d1 = {1:"a", 2:"b"}
d2 = dict({1:"a", 2:"b"})
d3 = dict(zip((1,2),("a", "b")))
d4 = dict([[2,"b"], [1, "a"]])
d5 = d1

print(d1 is d2)   #若為True則代表共用同一個物件(共用空間) d1做更動，d2也會做更動
print(d1 is d3)
print(d1 == d2)   #看值是否相等
print(d1 == d3)
print(d1 == d4)
print(d5 is d1)


d1 = dict()  #空字典
d1
#新增資料(直接用key加)
d1[8] = 99   #可直接在空字典的特定的key上加上新的物件，這是list無法用index(索引)辦到的
8 in d1  # 判斷d1內是否有8的索引值(只能找key，不能判斷字典裡的value)
9 not in d1

d1["a"] ="apple"

d1.keys()  #取得他所有的keys
d1.values() #取得他所有的values
d1.pop(8)  #刪除哪一個key所代表的資料  ()內填的是key的名稱  不能省略
d1.clear() #清空字典

#用字典的key來做迴圈
d = dict(zip((1,2,3,4),("a","b","c","d")))
for i in iter(d):   #iter可加可不加
    print(i, end = "\n")


#除了pop指令有回傳值的同時也對變數內容做了修改，
#其餘指令通常只要有回傳值就不會更改變數內容，
#只要會改變變數內容者就不會有回傳值(print 不出來)




# set 集合 (和dictionary 一樣都是使用大括號)但是是沒有順序的
continents = {"California", "New York"}
cities = {"New York", "Phonix", "Chicago"}
print(continents, "\n", cities, "\n", sep = "")

#清空集合 複製集合
continents.clear()  #清空
print(continents, "\n")
continents.copy()   #複製


#對集合加入元素
continents.add("Texas")
continents.add("California")
continents.add("New York")
print(continents, "\n")


#對集合移出元素
cities.remove("Chicago") #若沒東西可以回傳，會出現error
print(cities, "\n")
cities.pop() #移出集合內部的任一一個元素
print(cities)
continents.discard("California")   #若沒有東西出現，甚麼東西皆不會有
print(continents, "\n")


#集合間的運算與子集
cities.union(continents) #單純取聯集  重複的只會取一份
cities.update(continents) #取完聯集後覆蓋到.前面的變數(cities)
print(cities)
cities.difference(continents) #取差集
cities.difference_update(continents) #取完差集後覆蓋到.前面的變數(cities)
cities - continents #取差集
print(cities)
cities.intersection(continents) #取交集
cities.intersection_update(continents) #取完交集後覆蓋到.前面的變數(cities)
print(cities)
cities.issubset(continents) #前面集合(cities)是否是後面集合的子集(continents)
cities.issuperset(continents) #後面集合(continents)是否是前面集合的子集(cities)

#聯集減交集可以用 ^ 符號來表示 (此為X OR )
continents = {"California", "New York"}
cities = {"New York", "Phonix", "Chicago"}

union = cities.union(continents) #單純取聯集  重複的只會取一份
inter = cities.intersection(continents) #取交集
print(union)
print(inter)
print(union - inter)
print(cities ^ continents)
