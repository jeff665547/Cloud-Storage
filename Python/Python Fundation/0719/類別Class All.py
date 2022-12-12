#類別 物件 class  
#物件e.g.水瓶
#類別class 為物件設計的模板
#用class去把屬性給包起來
#凡是物件都會有屬性以及方法
#用屬性(attribute)(e.g. 外觀、顏色、容量大小、材質......)去描述物件
#屬性似變數
#方法:只有某一個物件才可以使用的(e.g. 裝水、喝水、倒水)
#方法似函數(用來操作自己(or別人)的屬性)
#屬性有分實體屬性或是類別屬性(其中類別屬性較少去用到，實體屬性較常用到(尤其是在其他語言更是如此))
#類別屬性:所有(同類別的)物件共有的(共用的變數)
#實體屬性:該物件自己所特別擁有的 所以通常會加上關鍵字"self"
#物件實體:就是指經由class這個模板所造出來的物件

#定義類別 class   classname
class Demo:
    i = 100 #i為類別屬性(前面不會有self.，直接放在class底下)
    def hello(self):   #方法
        print("hello")
#到這邊一個class(模板)就定義完了
help(Demo) #可以知道裡面有哪些東西
print(dir(Demo)) #可以知道裡面有哪些東西是可以使用的

class pokemon:
    ct = 0 #類別屬性 為大家共用的
    def attack(n):  #方法
        pass
    def defence(n):
        pass
    def cure(n):
        pass
    def showInfo(self):  #第一個參數都會放self，意思是把物件實體給丟進來
        print("Pokemon Info:")

help(pokemon)
print(dir(pokemon))
#output
# __main__ 代表主程式執行
#方法會按照字幕的順序排序
#dir印出的結果中若有  __  __  代表一些內建的方法(可忽略)，直接看沒些標記的方法


#這邊可以把它想成是class是模具，要準備生物件出來的概念
class Demo:
    i = 100  
    def hello(self):  
        print("hello")

d = Demo()  #d是利用模具所產生出來的物件，打. 就可以利用它裡面的東西(方法，屬性)
print(type(Demo))
print(type(d))
print(d.i) #d是利用模具所產生出來的物件，打. 就可以利用它裡面的東西(不管是實體屬性或是類別屬性都可以透過這樣的方法給拿出來)
d.hello()



#example
class pokemon:
    ct = 0 #類別屬性 為大家共用的
    def __init__(self):
        self.name = "皮卡丘"
        self.lv = 10
        self.hp = 15
        self.hpMax = 15
        
    def attack(n):
        pass
    def defence(n):
        pass
    def cure(n):
        pass
    def showInfo(self):
        print("Pokemon Info:")
        print("Name:", self.name)
        print("Lv:", self.lv)
        print("HP: %d/%d"%( self.hp, self.hpMax))

help(pokemon)
print(dir(pokemon))

p1 = pokemon()
print(type(p1))     #p1是一個__main__.pokemon的型態 代表放在main底下的pokemon型態(可以忽略main，不用管它，是系統為了避免內建的型態受到使用者汙染)
print(type(pokemon))    #pokemon 是自己所定義的一個型態(type) 和 type(int) 一樣，也就是這裡的pokemon和int的地位是一樣的，代表著一種型態，p1就是由這種型態所創造出的物件實體
print(p1.ct)
p1.showInfo()


#
a = int()
a
type(a)

lst = list()
lst
type(lst)

type(int)

#__init__() 建構式(子)，可在物件實體建構好的瞬間自動執行該函式initial 
class Demo:
    def __init__(self):
        self.name = "Python" #這邊的.name就是指實體屬性，從這一行之後.name就都會存在了
    def hello(self):
        print("hello", self.name)
        
d = Demo()
print(type(Demo))
print(type(d))
print("d.name:%s"%d.name)
d.hello()

###example
class pokemon:
    ct = 0 #類別屬性 為大家共用的
    def __init__(self, na, l, hp, hpm):  #把這邊的區域變數(na, l, hp, hpm)存到前面的self裡面,self就相當於p1 或是p2，而這邊的__init__()代表的意思就是去實際把這個實體用制定的模組給建立起來，而放進的參數第一個就是self(沒有意外的話)
        self.name = na
        self.lv = l
        self.hp = hp
        self.hpMax = hpm
        pokemon.ct += 1   #這邊是類別屬性(前面加了pokemon的概念就像是加了global一樣，告知系統對這裡的全域變數(類別屬性)進行運算)
        #self.ct = 1  #實體屬性會去覆蓋掉類別屬性(若從實體這邊去看的話)，要去看真正的類別屬性就只能從類別名稱的方向去找e.g. pokemon.ct (不管是哪個物件實體，出來的實體屬性都是1)
        
    def attack(self,target):
        if self.hp <= 0:
            print(self.name, "已失去戰鬥力，不能攻擊")
            return()  #直接跳出此function，不執行後續程式
        if target.hp <= 0:
            print(target.name, "已失去戰鬥力，不能攻擊他")
            return()
        print(self.name, "攻擊了", self.lv , target.name)
        target.defence(self.lv)
    def defence(self,n):
        self.hp -= n
        if(self.hp <= 0):
            self.hp = 0
            print(self.name, "失去戰鬥力")
    def cure(self):
        self.hp = self.hpMax
        print(self.name, "已痊癒")
    def showInfo(self): #這邊記得()裡要加self 代表的就是之後創建好的物件(p1, p2)，如果沒有寫self，底下將會辨別不出來self.name那些是甚麼東西
        print("Pokemon Info:")
        print("Name:", self.name)
        print("Lv:", self.lv)
        print("HP: %d/%d\n"%( self.hp, self.hpMax))

p1 = pokemon("皮卡丘", 10, 15, 15)
p1.showInfo()
p1.ct

p2 = pokemon("小火龍", 15, 25, 25)
p2.showInfo()
p2.ct

print("p1.ct = ", p1.ct)
print("p1.ct = ", p2.ct)
print("p1.ct = ", pokemon.ct)

p1.ct = 999         #新增實體屬性，不會覆蓋掉類別屬性
pokemon.ct = 888    #修改類別屬性的值

p1.attack(p2)
p1.showInfo()
p2.showInfo()
p2.attack(p1)
p1.attack(p2)
p2.attack(p1)

p1.cure()

#Class practice
class student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.grades = []
    
    def avg(self):
        return(sum(self.grades)/len(self.grades))
    
    def add(self, grade):
        self.grades.append(grade)
        
    def fcount(self):
        fct = 0
        for g in self.grades:
            if g < 60:
                fct += 1
        return fct
        
    def show(self):
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Grades:", self.grades)
        print("Avg: %.2f" %(self.avg()))
        print("Fail ct:", self.fcount())

s1 = student("小名", "男")
s1.add(10)
s1.add(60)
s1.add(90)
s1.show()
s1.avg()
s1.fcount()
