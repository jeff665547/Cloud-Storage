#例外處裡(error)
#一般來說出現紅字error就會停止執行，希望能越過這個障礙繼續執行
#目的是為了要預防使用者在輸入介面時亂輸入所造成的錯誤而造成阻礙
a = 10
b = 0

print(a/b)
print("hello python")

try:
    print(a/b)
except:             #此except後方沒有加入條件(錯誤類型)，代表不管發生甚麼錯誤，都可以進去接下來的程式碼作執行，不建議這樣的寫法，因為如果有錯誤的話會不知道是甚麼樣的錯誤類型                   
    print("例外發生，不可以除以0")
print("hello python")

#try: try是放你要偵測是否有錯的程式碼(通常是整個程式碼)
#except: except後面會放錯誤類型，一旦有異常發生的時候，程式會執行第一個符合該異常狀況的except(有點類似if和elif的感覺),except敘述可以有很多個
#else:  若在try的程式碼裡沒有發生異常，接著就會執行else裡面區塊內部的程式
#finally: 為最後執行的程式碼區塊，不管前面有無發生異常(以上的所有程式)，都會執行
#else 和 finally 這兩個方程式可寫可不寫

#ex:for 迴圈在try的外面，若有出現錯誤，則該次會進行例外處理，處理完後會繼續執行迴圈的其他值，不會受到錯誤的干擾，可以和下面的另一個例子做比較
i = 10

for j in range(3, -4, -1):
    try:
        print("%d/%d=%0.3f"%(i, j, i/j))
    except NameError:
        print("例外發生, NameError")
    except ZeroDivisionError:
        print("除數為0，無法進行除法")
    else:
        print("沒有例外發生")
    print("hello python")


#ex: for 迴圈在try裡面，一旦出現錯誤，就會從迴圈裏面跳出來並且終止迴圈的執行，可以和上面的例子做比較
try:
    print("進入try區塊")
    for i in range(5, -5, -1):
        print("10/"+str(i)+"=", end = "")
        print(str(10/i))
except:
    print("發生錯誤，進入except區塊")
    print("(except)i=" + str(i))
else:
    print("沒有錯誤，進入else區塊")
    print("(else)i=" + str(i))
finally:
    print("進入finally區塊")
    print("(finally)i=" + str(i))
    
    
#exercise
#利用input的方法，輸入兩個數字，並將兩個數字相除的結果印出。 
#加入例外處理機制，若發生任何例外則讓使用者重新輸入直到正確將相除的結果印出才終止程式。

while True:
    try:
        AA = eval(input("輸入數字a:"))
        BB = int(input("輸入數字b:"))
        ans = AA/BB 
    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        print(AA,"/", BB, " = %.2f"%(AA/BB), sep ="")
        break

#在此章節需要先看懂各個error代表甚麼錯誤
#e.g. 除以0 => ZeroDivisioneError
#e.g. 引入模組錯誤 => ImportError
#e.g. 型態錯誤 => TypeError
#在講義上有更多的錯誤類型

