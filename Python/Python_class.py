# 類別
class Demo:
    i = 100
    def hello(self):
        print("Hello")
help(Demo)         # 內建函數 help() 會顯示物件（包括類別）的資訊
print(dir(Demo))   # dir() 則會把物件（包括類別）的所有屬性與方法以串列 (list) 列出

d = Demo()   # Demo() 就是 Demo 類別建立物件的建構子 (constructor), 
             # 這裡利用指派運算子( = )將建構子( Demo() )所建立的實體物件 (instance) 給變數 d ，
             # 於是 d 就具有 Demo 型態的物件。
             # 利用建構子 (constructor) 建立的物件被稱為實體 (instance)，
             # 實際上建立物件的整個過程是執行 __init__() 方法 (method)。
print(type(Demo))   
print(type(d))
print(d.i)
d.hello()

# 自行定義的類別會有預先定義好的 __init__() ，
# 我們也可以改寫 (override) 成我們自己需要的
# 改寫方式就是再定義一次，方法的定義與函數 (function) 類似，
# 兩者同樣使用關鍵字 (keyword) def
class Demo2:
    def __init__(self):
        self.name = "Python"
    def hello(self):
        print("hello", self.name)

d = Demo2()
print(type(Demo2))
print(type(d))
print("d.name: %s"%d.name)
d.hello()
## 在 __init__() 所定義的實體屬性 (attribute) 都需要額外加上 self ，
## 如上方第3行的 self.name。
## 凡是實體(instance)的方法都需要一個特別的參數 -- self ， 
## self 是個預設的保留字 (reserved word) ，所指的是實體(instance)本身。

# 設定類別 __init__ 參數 (Constructor的參數)
class Demo3:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("Hello", self.name)
d = Demo3("Tom")
print(type(Demo))
print(type(d))
print("d.name:%s"%d.name)
d.hello()
## 帶入自訂的預設參數，加在self的後面

# 類別 __DOC__
# 類別 (class) 有 __doc__ 屬性 (attribute) ，
# 這是三引號字串定義的文字，屬於類別的說明文件。
class Demo4:
    '''
    Demo Document:
     hello python
    '''
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("hello", self.name)
d = Demo4("Tom")
print(help(d))


# 類別屬性與實體屬性
class Demo5:
    x = 0;     # x 為類別屬性，Demo5類別的屬性
    '''
    Demo Document:
     hello python
    '''
    def __init__(self, i):
        self.i = i          # self.i則為實體屬性
        Demo5.x += 1
    def hello(self):
        print("hello", self.i)
        
print("There are", Demo5.x, "instances.")
a = Demo5(1122)
a.hello()
print("a.x=", a.x)
print("a.i=", a.i)
b = Demo5(3344)
b.hello()
print("b.x=", b.x)
print("b.i=", a.i)
c = Demo5(5566)
c.hello()
print("c.x=", c.x)
print("c.i=", a.i)
d = Demo5(7788)
d.hello()
print("d.x=", d.x)
print("d.i=", a.i)
e = Demo5(9900)
e.hello()
print("e.x=", e.x)
print("e.i=", a.i)
print("After all, there are", Demo5.x, "instances.")

## 若是類別屬性與實體屬性的識別字相同,實體物件只能存取實體屬性,不會影響類別屬性的值,
## 但若不相同，實體物件能存取類別屬性的值。
class Demo6:
    i = 0
    '''
    Demo Document:
       Hello Python
    '''
    def __init__(self, i):
        self.i = i
        Demo6.i += 1
    def hello(self):
        print("hello", self.i)
print("There are", Demo6.i, "instances.")
a = Demo6(1122)
a.hello()
print("a.i = ", a.i)
b = Demo6(3344)
b.hello()
print("b.i=", b.i)
c = Demo6(5566)
c.hello()
print("c.i=", c.i)
d = Demo6(7788)
d.hello()
print("d.i=", d.i)
e = Demo6(9900)
e.hello()
print("e.i=", e.i)
print("Afetr all, there are", Demo6.i, "instances.")

# Advc Topic
# Python class 屬性封裝
## Python 類別 (class) 的屬性 (attribute) 權限預設是公開的，
## 因此類別以外的地方也可以存取，例如
class Demo7:
    x = 0
    def __init__(self, i):
        self.i = i
        Demo7.x += 1
    
    def hello(self):
        print("Hello", self.i)
    
a = Demo7("Tom")
a.hello()           # public的屬性以及方法可在外部存取
print("Hello", a.i)   # public的屬性以及方法可在外部存取
print()
print("a.i = ", a.i)
print("Demo7.x = ", Demo7.x)  # public的屬性以及方法可在外部存取

# 受保護的屬性
# 在屬性的前面加上雙底線「__」即變成受保護的屬性
# e.g.
class Demo8:
    __x = 0   # protected members
    def __init__(self, i):
        self.__i = i   # protected members
        Demo8.__x += 1
    def hello(self):
        print("Hello", self.__i)
        
a = Demo8("Tom")
a.hello()
print("Demo.x=", Demo.__x)  #受保護而不能存取
print("Demo.i=", Demo.__i)  #受保護而不能存取


# 類別方法
# 回傳受保護屬性時，類別方法需要一個特別的參數 (parameter) ，
# 習慣上使用 cls ，這與實體方法的 self 類似，
# 不同的是 cls 用來存取類別的屬性 (attribute)，而非物件實體。
# 格式如下:
#
# @classmethod
# def function_name(cls):
#    return cls.__變數    ## 回傳受保護的屬性
#
#e.g.
class Demo9:
    
    __x = 0  # protected members of the class
    def __init__(self, i):
        self.__i = i  # protected members of the instance
        Demo9.__x += 1
    def hello(self):
        print("hello", self.__i)
        
    @classmethod
    def getX(cls):
        return cls.__x

a = Demo9("Tom")
a.hello()
print("Demo9.__x=", Demo9.getX())
## 方法預設也都是公開的，若要定義私有的方法，也就是只能在類別內呼叫的方法，
## 同樣在方法識別字名稱前加上連續兩個底線符號，這樣的方法就變成私有的。


# 繼承 (Inheritance)
# 若定義了很多類別 (class) ，這些類別中又具有相當多相同的屬性 (attribute) 
# 或方法 (method) 定義，這時候，可利用 Python 的繼承 (inheritance) 機制。
# 將共通的屬性及方法提取出來，另行定義父類別 (superclass) ，py


# 然後將原本提出共通屬性及方法改為繼承 (inherit) 父類別的子類別 (subclass)
# 格式如下:
# 
# class SubDemo(Demo):
#   #dosomething
#
# 這是從 SubDemo 類別去繼承 Demo ，注意類別名稱後的小括弧中註明父類別。
#
#e.g.
class Demo10:
    __x = 0
    def __init__(self, i):
        self.__i = i
        Demo10.__x += 1
    def hello(self):
        print("hello", self.__i)
    @classmethod            #類別方法1
    def getX(cls):
        return cls.__x
    @classmethod            #類別方法2
    def add(cls):
        Demo10.__x += 1
        
class subDemo10(Demo10):
    pass #略過
    
a = Demo10("Tom")
a.hello()
b = subDemo10("John")
b.hello()
print("Demo10.x = ", Demo10.getX())


# 內建函數
# 內建函數 (function) isinstance() 可以判斷某一個物件是否為某一個類別所建構的實體 
# (instance) ，若真則回傳 True ，否則回傳 False。
# 另一個內建函數 issubclass() 則可以判斷某一個類別是否為另一個類別的子類別，
# 同樣的，若真則回傳 True ，否則回傳 False 。
# e.g.

a = Demo10("Tom")
b = subDemo10("John")

print(isinstance(a, Demo10))  #isinstance
print(isinstance(a, subDemo10))
print(isinstance(b, Demo10))
## 變數 (variable) b 雖然是由 SubDemo 建立的，但是 b 也會是 Demo 的實體，
## 這是由於物件實體的建構過程中，會先建立父類別的部份，
## 因此也會建立屬於 b 的父類別物件實體，使 b 得以運用父類別的屬性及方法。
print(isinstance(b, subDemo10))
print(issubclass(subDemo10, Demo10))  #issubclass
print(issubclass(Demo10, subDemo10))


# 子類別 方法改寫
# 子類別 (subclass) 可依本身特性設定自己的屬性 (attribute) 與方法 (method) ，
# 也會從父類別 (superclass) 繼承 (inherit) 屬性與方法。
# 一般來說，沒有設定成私有的屬性及方法都會被繼承，
# 子類別可由父類別公開的方法存取父類別私有的屬性。
# 子類別也可依需要改寫 (override) 父類別的方法，
# 這是說子類別需要用到與父類別具有相同名稱的方法，
# 但是子類別需要的功能有所修改、擴充或增加，
# 因此當子類別裡頭定義與父類別相同名稱的方法時，就會改寫父類別的方法。
# 經過改寫，子類別的方法完全屬於子類別所有。
# e.g. 

class Demo11:
    __x = 0
    def __init__(self, i):
        self.__i = i
        Demo11.__x += 1
    def hello(self):
        print("hello", self.__i)
    @classmethod
    def getX(cls):
        return cls.__x
    @classmethod
    def add(cls):
        Demo11.__x += 1
            
class subDemo11(Demo11):
    def __init__(self, i, j):
        self.__i = i
        self.__j = j
    def hello(self):
        print("hello", self.__i, self.__j)
        
a = Demo11("Tom")
a.hello()
print("Demo.x=", Demo11.getX())   # ans: x = 1
b = subDemo11("John", "Mary")
b.hello()
print("Demo.x=", Demo11.getX())   # ans: x = 1


# super() 呼叫父類別的方法
# 利用內建函數 (function) super()，呼叫 (call) 父類別的方法
# e.g.
class Demo11:
    __x = 0
    def __init__(self, i):
        self.__i = i
        Demo11.__x += 1
    def hello(self):
        print("hello", self.__i)
    @classmethod
    def getX(cls):
        return cls.__x
    @classmethod
    def add(cls):
        Demo11.__x += 1
            
class subDemo11_2(Demo11):
    def __init__(self, i, j = "guest"):
        self.__i = i
        self.__j = j
    def hello(self):
        print("hello", self.__i, self.__j)
    def superHello(self):
        super().__init__(self.__i)
        super().hello()
        
a = Demo11("Tom")
a.hello()
b = subDemo11_2("John", "Mary")
b.hello()
print("Demo.x = ", Demo11.getX())
b.superHello()
print("Demo.x = ", Demo11.getX())



# 類別 多重繼承
# 設計類別 (class) 時，父類別 (superclass) 可以有多個，
# 這是說子類別 (subclass) 能夠繼承 (inherit) 多個父類別，使子類別可以有多種特性。
#　這裡須注意一點，當子類別繼承 (inheritance) 超過一個來源的時候，
#　會以寫在最左邊的父類別優先繼承，這是說，
# 多個父類別如果有相同名稱的屬性 (attribute) 與方法 (method) ，
# 例如 __init__() 、 __str__() 等，就會以最左邊的父類別優先。
# e.g.
class Demo12:
    __x = 0
    def __init__(self, i):
        self.__i = i
        Demo12.__x += 1
    def hello(self):
        print("hello", self.__i)
    @classmethod
    def getX(cls):
        return cls.__x
    @classmethod
    def add(cls):
        Demo.__x += 1

class Demo13:
    def __init__(self, i):
        self.__i = i
    def reverseString(self, string):
        reverse = ""
        for i in range(len(string)-1, -1, -1):
            reverse += string[i]
        return reverse

class subDemo12(Demo13, Demo12):
    def __init__(self, i, j = "guest"):
        super().__init__(i)
        self.__i = i
        self.__j = j
    def hello(self):
        print("hello", self.__i, self.__j)
    def superHello(self):
        super().__init__(self.__i)
        super().hello()

a = subDemo12("Tom")
print(a.reverseString("Tom"))
print("Demo.x = ", Demo12.getX())


# Destructors 解構子  (__DEL__())
# 建構子 (constructor) 用來建立物件 (object) ，
# 當物件不需要被使用時，直譯器 (interpreter) 會主動替物件呼叫 __del__() 方法 (method) ，
# 這是物件自動銷毀的方法，也就是從記憶體中釋放空間的步驟，
# 被稱為解構子 (destructor) ，當然，我們也可以改寫 (override) 這個方法。
class Demo14:
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return str(self.i)
    def __del__(self):
        print("del called:" + self.__str__())
    def hello(self):
        print("hello " + self.__str__())

a = Demo14("Tommy")
a.hello()
a = Demo14("gg")
b = Demo14("Tommy")
a = 1
a = Demo14("cc")
del a
## 我們只有使用變數 (variable) a 一個名稱，
## 利用建構子 Demo() 建立物件後呼叫 hello() ，
## 然後重新呼叫 Demo() 建立另一個 Demo 型態的物件，
## 我們可以看到直譯器主動呼叫 __del__() ，
## 印出 "del called" 的訊息。
## 最後程式結束執行前，直譯器同樣主動呼叫最後建立物件解構子，完全釋放所使用的記憶體空間。



# 多型　(Polymorphism)
# 多型 (polymorphism) 是物件導向程式語言 (object-oriented programming language) 
# 的一項主要特性，使物件 (object) 的使用更具彈性。
# 比如有動物（Animal）之類別（Class），而且由動物繼承出類別雞（Chicken）和類別狗（Dog），
# 並對同一源自類別動物（父類別）之一訊息有不同的響應，如類別動物（Animal）有「叫()」之動作，
# 而類別雞（Chicken）會「啼叫()」，類別狗（Dog）則會「吠叫()」，則稱之為多型。
# 簡單來說，多型可使物件的型態具有通用的效力，例如以下程式
class Demo15:
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return str(self.i)
    def hello(self):
        print("hello" + self.__str__())

class SubDemo15_1(Demo15):
    def __init__(self, i, j):
        super().__init__(i)
        self.j = j
    def __str__(self):
        return super().__str__() + str(self.j)

class SubDemo15_2(Demo15):
    def __init__(self, i, j):
        super().__init__(i)
        self.j = j
        self.k = str(self.i) + str(self.j)

    def __str__(self):
        return self.k

a = SubDemo15_1(22, 33)
b = SubDemo15_2(44, "55")
a.hello()
b.hello()
## 不同的物件但卻有相同的attribute，但執行結果卻是不同的


# 多型　（其他的例子）
d1 = "12345"
d2 = [1, 2, 3, 4, "5"]
print(d1.count("4"))
print(d2.count("4"))
## d1 為字串 (string) ， d2 為串列 (list) ，
## 兩者皆屬於序列 (sequence) 的複合資料型態 (compound data type) ，
## 有通用的 count() 方法，可計算某元素 (element) 累計出現的次數。
## 多型的應用很多，例如串列中可接受不同型態的物件當元素，或是方法可用不同型態的參數等。
