import sys
from PyQt5.QtWidgets import QWidget

# dir() 查詢一個類別或物件的所有屬性以及方法(函數)
# help() 用來查詢類別的說明文件
dir(QWidget)
help(QWidget)

# lambda expression 
fun1 = lambda x, y: x + y
print('fun1(2, 3) = ', fun1(2, 3))

fun2 = lambda x: x^2
print('fun2(4) = ', fun2(4))

# Class and Instance
#%%
class MyClass:
    # 類別變數
    count = 0
    name = 'DefaultName'
    
    def __init__(self, name):  #類別的方法必須包含參數self，且為第一個參數
        self.name = name 
        print("Class var: {}, Inst var: {}".format(MyClass.name , self.name))
    
    # MyClass.name 取用類別變數 (<class name>.<var name>)
    # self.name 取用物件實例變數 (self.<var name>)
    
    def setCount(self, count):
        self.count = count
        
    def getCount(self):
        return self.count

#%%
class MyCounter:
    __secretCount = 0  # 類別私有屬性(私有類別變數) ==> 以兩個底線開頭，只能用於類別內部    
    # 不能在類別外面呼叫以及存取
    
    publicCount = 0    # 類別公共屬性(公共私有變數)
    
    # 類別變數就是一個類別的全域變數，類別產生實體以後的物件都可以使用該變數。
    
    def __privateCountFun(self):  # 不能在類別外面呼叫
        print("This is a private method")
        self.__secretCount += 1   # 使用私有類別變數
        self.publicCount += 1     # 使用公共類別變數
        #print(self.__secretCount)
        
    def publicCountFun(self):  # 不能在類別外面呼叫
        print("This is a public method")
        self.__privateCountFun()
        
        
#%% 類別的動態屬性
#  使用時機: 類別中的某個私有屬性需要根據不同的動作(讀取、賦值(更改)、刪除)
#            來進行不同的權限控管時。
        
#
#3 以類別屬性存取類別的私有變數
class MyClass2(object):
    def __init__(self):
        self.__param = None
        
    def getParam(self):
        print("get param: {}".format(self.__param))
        return self.__param
    
    def setParam(self, value):
        print("set param: {}".format(self.__param))
        self.__param = value
        
    def delParam(self):
        print("del param: {}".format(self.__param))
        del self.__param
        
    param = property(getParam, setParam, delParam)  
    # 利用property 函數來 define setter, getter, and deleter

#%%
#4 @property可以將python定義的函數"當作"屬性存取
# (@property使方法像屬性一樣呼叫，就像是一種特殊的屬性)
class MyClass3(object):
    def __init__(self):
        self.__param = None
        
    @property
    def param(self):
        print("get param: {}".format(self.__param))
        return self.__param
    
    @param.setter
    def param(self, value):
        print("set param: {}".format(self.__param))
        self.__param = value
        
    @param.deleter
    def param(self):
        print("del param: {}".format(self.__param))
        del self.__param

#%%.
#5  如果在外部想要給param重新直接賦值就會報
#   AttributeError: can’t set attribute的錯誤，這樣就保證了屬性的安全性。
#   如果在外部想要刪除param就會報
#   AttributeError: param is not deletable attribute.
class MyClass4(object):
    def __init__(self):
        self.__param = None
        
    @property
    def param(self):
        print("get param: {}".format(self.__param))
        return self.__param
            
    @param.deleter
    def param(self):
        print("del param: {}".format(self.__param))
        raise AttributeError('param is not deletable attribute.')

#%% 類別繼承
# Python的類別都繼承自object
# 繼承的語法，e.g. class Andy(Employee):
# super 是呼叫父類別的語法，如果子類有與父類同名的函式，則子類會覆蓋掉父類的函式。
# super(class, self).method() 是去呼叫 class 父類別 (parent of class) 中的 method 方法。
# 在 Python3 中 super().method() 相當於 super(class, self).method()
# 繼承後即可調用父類別的屬性以及函數, e.g. getDetials(self): 中的 self.cut_tree
# 在 Python3 中 class Employee: 寫法相當於 class Employee(object): 寫法, 
# 在 py3 中系統會自動加載 object (即便沒有寫object)
# 在 Python2 中 class Employee: 寫法所涵蓋的功能較 class Employee(object): 寫法來的少

class Employee:   
    def __init__(self):
        self.cut_tree = 3
        
class Andy(Employee):
    def __init__(self, get_gold):
        super().__init__() # 相當於super(Andy, self).method(), 呼叫Andy父類別(Employee)的__init__函式
        self.get_gold = get_gold
        
    def getDetials(self):
        print("==getDetails==")
        print('tree:', self.cut_tree)
        print('gold:', self.get_gold)


#%% 類別封裝
# 封裝從字面上理解就是包裝的意思，像是打電話，我們都不知道背後具題實現細節，
# 但只需要按下按鈕就可以完成，這功能就是封裝。
# 專業點來說就是指隱藏程式實現細節只保留下其接口，使程式容易模塊化。
# 下面範例 work() 就是封裝的表現，可以讓外部使用者不需考慮內部實作而直接呼叫使用。
# 若是有不想被呼叫的變數，直接在前面加上 __  (雙底線)像是 __sleep即可以成為私有變數，
# 如果使用者呼叫 __sleep 時則會報 object has no attribute 的錯誤。
class Employee2:
    def __init__(self):
        self.cut_tree = 3
        
    def work(self):
        print("Working")
        
    def __sleep(self):
        print("Sleeping")
        
        
#%% 類別多型
# 呼叫同名的方法時會去執行不同方法實作，則屬於「多型(polymorphism)」的表現形式。
# 下面範例 Employee3 類別的 work() 方法在 Andy3 類別以及 Joy 類別被覆蓋掉了，所以在呼叫 w1.work() 時，
# Python 會根據w1所屬的類(Andy3)來決定要執行哪個方法實作，這就是多型的意思。
class Employee3:
    def work(self):
        print("Employee work")
        
class Andy3(Employee3):
    def work(self):  # 子類有與父類同名的函式，子類會覆蓋掉父類的函式。
        print("Andy work")
        
class Joy(Employee3):
    def work(self):  # 子類有與父類同名的函式，子類會覆蓋掉父類的函式。
        print("Joy work")

#%%
if __name__ == "__main__":
    cls = MyClass('lisi')
    cls.setCount(10)
    print("count = {}".format(cls.getCount()))
    
    counter = MyCounter()
    counter.publicCountFun()
    counter.publicCountFun()
    print("Instance publicCount = {}".format(counter.publicCount))
    print("Class publicCount = {}".format(MyCounter.publicCount))
    
    #3
    cls = MyClass2()
    cls.param = 10
        
    print("current param: {}".format(cls.param))
    del cls.param
        
    #4 
    cls = MyClass3()
    cls.param = 10
        
    print("current param: {}".format(cls.param))
    del cls.param
    
    #5
    cls = MyClass4()
    cls.param = 10
        
    print("current param: {}".format(cls.param))
    del cls.param
    
    #類別繼承
    andy = Andy(1)
    andy.getDetials()
    
    #類別封裝
    Andy = Employee2()
    Andy.work()
    Andy.__sleep()
    
    #類別多型
    w = Employee3()
    w1 = Andy3()
    w2 = Joy()
    
    w.work()
    w1.work()
    w2.work()
