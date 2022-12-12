interger1=interger2= interger3= 10
string1, float1 ="test", 12.0
print(interger1, interger2, interger3, string1, float1, sep =",")
print(interger2, interger3, string1, float1, sep =",")
10,10,test,12.0
string1, float1 = float1, string1
print(interger1, interger2, interger3, string1, float1, sep =",")
10,10,10,12.0,test
numbers = [1,2,3]
print(numbers)
print(numbers)
[1, 2, 3]
2+3  #加
3-9  #減
5*8+1  #乘
3**2   
2**10  #次方
2/5    #回傳商(全部的值，包含小數點)
9/10   
3//5   #回傳商(整數部分)
6//5
9//3
9//4
9//5
9//6
9//7
9//8
9//9
9//10
9//2
9.5//2  
6/3
6%3
6%4
6%5
6%6   #回傳餘數(mod)
elfCoins =5000
elfCoins = elfCoins - (1000+1500)
elfCoins = elfCoins - 2000*0.75
print("還剩下", elfCoins, "精靈幣")
up = 10
down = 15
heigh = 7
(up + down)*heigh/2
area = (up + down)*heigh/2
print("The area is ", area)
print(2 ==2 )
print(2 != 2)
print(6>4)
print(4<6)
print(6>=3)
print(6<=3)
interger = 7
print( 5 < interger <= 10)
list1 = [1, "test"]
list2 = [1, 'test']            
print(list1 == list2)
print(list1 is list2)
list1 = list2
print(list1 is list2)
print(list1 == list2)
list2 = [1, "test"]
print(list1 == list2)
print(list1 is list2)
string1 = "test"
string2 = "test"
print(string1 == string2)
print(string1 is string2)
# complex number(j)
type(3) #類型判斷 回傳((資料型態:float, complex, bool, string(str), integer(int)),(資料結構:list))
#轉換變數類型所使用的函數名稱和上面類型判斷裡的名稱是一樣的(float(), complex(), bool(), str(), int())
bool(1000)
bool(0) #只有0會變False, 其他的都是True
#in 是否包含於 & not in 是否不包含於
#e.g.
7 in [1,3,5,7,9]
"7" not in [1,3,5,7,9]
#格式化輸出 print with format
print("我的身高是: %s 公分; \n體重是: %i 公斤; \nBMI是: %.2f" % (172, 67, 22.654321))
#python 原生資料結構
#原始環境中不支援跳著選的索引值，只能連著選e.g.[0:2] => 0,1
#tuple, list, dictionary, set
#套件資料結構
#ndarray(In numpy), dataframe(In pandas)
#ndarray支援跳著選的索引值
#
#list裡面也可以再放list與其他種資料結構
#==================== RESTART: C:/Users/user/Desktop/HW.py ====================
"""
圓周率 3.141592653589793
半徑 100
圓周長 628.3185307179587
圓面積 31415.926535897932
#==================== RESTART: C:/Users/user/Desktop/HW.py ====================
100
圓周率 3.141592653589793
半徑 100
圓周長 628.3185307179587
圓面積 31415.926535897932
"""
#=================== RESTART: C:/Users/user/Desktop/HW2.py ===================
87.5
#=================== RESTART: C:/Users/user/Desktop/HW2.py ===================
10
15
7
87.5

#流程控制
#=================== RESTART: C:/Users/user/Desktop/HW3.py ===================
60
及格
#=================== RESTART: C:/Users/user/Desktop/HW3.py ===================
60
pass 
#=================== RESTART: C:/Users/user/Desktop/HW4.py ===================
"""
95
獎金 2000 元
 
#=================== RESTART: C:/Users/user/Desktop/HW4.py ===================
100
獎金 2000 元

=================== RESTART: C:/Users/user/Desktop/HW4.py ===================
95
獎金 2000 元
>>> 
=================== RESTART: C:/Users/user/Desktop/HW4.py ===================
95
獎金 2000 元
>>> 
=================== RESTART: C:/Users/user/Desktop/HW4.py ===================
60
獎金 0 元
>>> 
=================== RESTART: C:/Users/user/Desktop/HW4.py ===================
95
獎金 2000 元
>>>
""" 
#=================== RESTART: C:/Users/user/Desktop/HW4.py ===================

#=================== RESTART: C:/Users/user/Desktop/HW5.py ===================
6
7
9
9
 
#=================== RESTART: C:/Users/user/Desktop/HW5.py ===================
99
66
57
99
 
#=================== RESTART: C:/Users/user/Desktop/HW6.py ===================
55
99
100.000
100.00
99
99
99
99

#=================== RESTART: C:/Users/user/Desktop/HW6.py ===================
99
99
100.000
100.00

import random
random.randint(1, 5)

print(range(4, 20, 2))
random.choice(range(4, 20, 2))
random.choice("hello")
random.choice([1, 2, 5, 8, 10, 300, 54, 61, 39])



