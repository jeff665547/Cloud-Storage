
import random

Ans = random.randint(1, 5)

guess = eval(input("請猜一1到5的號碼:"))
if(guess == Ans):
    print("你猜對了 ! 答案正是 ", Ans)
else:
    print("你猜錯了喔~其實是", Ans)