#function 函數
#自訂函數與內建函數
ls = [99, 88, 77]
sorted(ls) #此為函式，會有回傳值

ls.sort() #此並非函式，沒有回傳值，需要另外打variable才能把值給弄出來
ls

#function後面的括號裡的變數可以有很多個，只要加上逗號隔開即可，也可以沒有
#沒有回傳值的函數把它給print出來會得到none的結果
#return 代表之後的程式碼不會被執行，為結束函式並且回傳function 值
#return 只能回傳一個值，若丟多個值進去(用逗號分隔)，則會回傳一個tuple的形式
def hello():
    print("hello", 1 )
    print("hello", 2 )
    print("hello", 3 )

print("before hello")
hello() #沒有回傳值，但原本 function 裡面就帶有print的功能，所以會印出來
print("after hello")
print(hello()) #沒有回傳值，但原本 function 裡面就帶有print的功能，硬要print就只會得到None的結果
print("last hello")
print(hello) #後面的編碼為記憶體位置

#函式內的變數為區域變數，出了函式之後都不能再被呼叫，都不能再被使用
#要先定義函式接著再呼叫該函式
#預設參數(沒預設到的參數若使用者也沒有輸入，結果就會爆掉)
#function後的參數擺放位置可不按照順序對應，但前提是要加入參數名稱
def PrintData(uid, name = "No name", age = 0):
    print("The user id:", uid)
    print("The username:", name)
    print("The user age:", age)

PrintData(1, "John", 20)
PrintData(2, "May")
PrintData(3)
PrintData() #沒給uid(因為其沒有給定預設值)，會有error
PrintData(age = 20, name ="John", uid = 0)
PrintData(name ="May", uid = 1)

#return 只能回傳一個值，若丟多個值進去(用逗號分隔)，則會回傳一個tuple的形式，把多個值給包起來
import random

def rand2int():
    rand1 = random.randint(1, 10)
    rand2 = random.randint(1, 10)
    return(rand1, rand2)

a,b = rand2int()
print(a)
print(b)
print(rand2int())

#函數   不限定(或未知)傳入參數的個數  
#*是tuple  **dictionary 
#*後面是加tuple或是dictionary的名稱
#注意函數的括號內放的不是一個tuple，而是一組物件，中間由逗號隔開e.g.hello("Tom", "Peter", "Bob", "Rain")，
#並非hello(("Tom", "Peter", "Bob", "Rain"))
def hello(*names):
    for n in names:
        print("Hello, %s."%n)

hello("Tom", "Peter", "Bob", "Rain")

#**dictionary 中  等號前面會自動變key，後方會自動變value，最後出來的結果順序會和一開始的不同，因為字典是無序的
def hello(**names):
    for n in names:
        print("Hello", n, end = ", ")
        print("you are", names[n], "years old")

hello(John = 25, Tom = 20, Bob = 33)



#傳遞數值(字串)參數   參數內容會被copy 到函式用來接收參數的變數中
#copy 完後就變新的變數
def passValue(args):
    print(" before change:", args)
    args = 999
    print(" after change:", args)
    
num = 10       
print("before call:", num)
passValue(num)
print("after call:", num)

#傳遞容器參數     (整個容器都傳進去，而非容器內部某一個特定的性質)   
#參數內容不會被copy到函式用來接收參數的變數中
#而是直接assign 到同一個記憶體位置
#所以原本的值會有更動, 要用.copy來避免情況發生

def passList(lst):
    print(" before sort:", lst)
    lst.sort()
    print(" after change:", lst)
    
list1 = [44, 63, 7, 22, 5, 1]
print("before call:", list1)
passList(list1)
print("after call:", list1)




#函數產生器 yield    為一個可以回傳多"次"值的方法(一般如果用return的話後續的程式就不會再繼續跑了)
def gen(n):
    for i in range(1, n+1):
        print("In func", i)
        #return i   用return的話後續的程式就不會再繼續跑了,因此在這裡就只會回傳第一個i值
        yield i
print(gen(10))  #單純這樣不會有東西
print(list(gen(10))) #給他一個裝回傳值的容器，系統就會用容器把回傳值給包起來。
print(tuple(gen(15))) #用tuple 包
print(set(gen(13))) #用set包


#全域變數，區域變數間的關係(全域變數不能使用區域變數的值，函式外面不能使用函式內部(區域變數)的值)
#若在區域變數也有定義過和全域變數一樣的變數名稱，則跑函數時會以區域變數所定的值為主，全域變數的值就會被蓋掉，會以區域變數的值為優先使用
#建議:全域變數和區域變數的名稱不要重複，避免造成混淆
#注意func的()內並無東西
def func():
    x = 2
    x = x + 1
    print("In func():", x)

x = 1
func() #x=2+1=3 區域變數
func() #x=2+1=3 區域變數 x重新賦予一次2的值
print(x) #x=1  全域變數

############## Another example ##############
def func1():
    x = 10
    print("In func1:", x)
def func2():
    x = 20
    print("In func2:", x)

x = 1
func1()
func2()
print(x)     
     
#注意:
#但若為底下這樣的形式，就不能把變數y給放在等號左邊，除非強制宣告成global更改，否則僅能單純讀取全域變數的值。
#注意def func()的()內並無東西，代表整個物件都要被丟進這個程式裡面，若有放其他的變數(e.g.接下來的幾個例子)
def func():
    #global y  #強制去改變全域變數的值
    #y += 1   #此行若上面沒有global的指令則會造成系統混亂，系統會不知道說你是要命名一個新的區域變數還是要去更改原始全域的值，會有問題(程式會先從等號右側的y+1開始跑，在此時的y值是拿全域變數的y(=10)來跑，跑完之後才會賦予回去給等號左側的y值，但此時系統會錯亂不知道等號左側的y值是區域變數還是全域變數)
    print("In func():", y)

y = 10
func() 
func() 
print(y) 

############## Another example ##############
name = "John"
def change(n):
    #global name   #有或沒有這一行都是可以執行的，但是結果會不相同，一個的執行結果會把name變成是全域變數，另一個就還是原本的區域變數
    name = n  #沒有上面global的話代表是區域變數，有上面global的話就會變成是全域變數
    print("change name", name)
print("outside function", name)
change("Jack")
print("outside function", name)


#一般參數傳遞 (函式裡面有另一個函式,can be used only in python!!!)
#注意outer()內有放參數，此處輸入因非容器，所以變數會被複製，而不是指到同一個物件共用空間
def outer(a):    
    def inner(a):
        a += 1
        print("inner a =", a)
    a += 1
    inner(a)
    print("outer a =", a)

a = 10
print("global a =", a)
outer(a)
print("global a =", a)

#如果加入global 變成混合型，但只要加global就是指全域變數(無任何條件)，也就是在還沒進入function前所給定的那個參數
#若只想以上一層的參數作為基礎，則要使用nonlocal
def outer(a):    
    def inner():
        global a
        a += 1     #因為是直接送入物件，所以沒有上面global a那行的話程式會錯
        print("inner a =", a)
    a += 1
    inner() #先跑上面那一行後才對global a動手腳
    print("outer a =", a)

a = 10
print("global a =", a)
outer(a)
print("global a =", a)

#nonlocal 就是單純往外找一層，如果只有一層的function的話就會變成是指全域的變數了
def outer(a):    
    def inner():
        nonlocal a
        a += 1
        print("inner a =", a)
    a += 1
    inner()
    print("outer a =", a)

a = 10
print("global a =", a)
outer(a)
print("global a =", a)

#簡易函式(一行寫完)
def func1(x, y, z):
    return x + y + z
func1(1, 2, 3)
#上下兩種寫法的意思都是相同的 lambda 參數: 要return的公式
func2 = lambda x,y,z : x + y + z
func2(1, 2, 3)

#map(func, *要送進前面function處裡的值(sequence))
#出來記得要選用一個容器去包它
my_list = [1, 2, 3]
tuple(map( lambda i: i * i, my_list))
list(map( lambda i: i * i, my_list))
set(map( lambda i: i * i, my_list))

#另一個例子
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def fn(x):
    return x*2
list(map(fn, a))







