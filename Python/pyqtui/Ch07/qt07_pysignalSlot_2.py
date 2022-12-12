# PyQt5 訊號與槽
# 每個QObject物件和PyQt所有繼承QWidget的控制項(皆是QObject的子物件)，
# 都支援訊號與槽機制。在PyQt5中，訊號與槽透過object.signal.connect()方
# 法連接
# PyQt5的控制項類別有很多內建訊號，開發者也可以自訂訊號。
# 訊號與槽具有以下特點：
# 1. 一個訊號可以連接多個槽
# 2. 一個訊號可以連接另一個訊號
# 3. 訊號參數可以是任何的Python類型
# 4. 一個槽可以監聽多個訊號
# 5. 訊號與槽的連接方式可以是同步連接或是非同步連接。
# 6. 訊號與槽的連接，可能會跨執行續。
# 7. 訊號可能會斷開。
# 
# 編寫類別時，必須先定義該類別的訊號與槽，並於類別中連接訊號與槽，
# 以實現物件之間的資料傳輸。
#
# 訊號與槽有三種使用方法:
# 1. 內建訊號與槽的使用
# 2. 自訂訊號與槽的使用
# 3. 裝飾器訊號與槽的使用 (為第1種方法的衍伸)
# 
# 本例介紹第二種方法: 自訂訊號與槽的使用
# (傳遞兩個參數，若為傳遞多個參數，要使用進階自訂訊號與槽)
# 自訂訊號與槽的使用指在發射訊號時不呼叫視窗控制項的函數，而是自訂的函數。
# 意即以pyqtSignal實例物件發射訊號。
# 使用內建函數只有在特定的情況(如按鈕的點擊事件)下，
# 才能發射一些較為常用的訊號。另外，內建函數只能傳遞特定的參數，無法自訂，
# 較不靈活。
# PyQt5.QtCore.pyqtSignal()函數能為QObject建立訊號，同時也把該
# 建立好的訊號定義為類別的屬性。
# 此外，必須在建立類別時定義好訊號，不能在之後作為類別的屬性動態增加。
# 以pyqtSignal()函數建立訊號時，可以傳遞多個參數，並指定這些參數類型，
# 這些參數類型為Python標準的資料類型。
# (字串、日期、bool、數字、list、tuple、dict)

import os
import sys
from PyQt5.QtCore import (QObject, pyqtSignal)

# 訊號物件(發送者)
class QTypeSignal(QObject):
    
    # 定義一個訊號
    # 此例為傳遞兩個物件參數 (或兩個字串參數)
    # 若為傳遞多個參數，要使用進階自訂訊號與槽
    sendmsg = pyqtSignal(object, object) 
    # 兩個字串參數也可以寫成: pyqtSignal(str, str)

    def __init__(self):
        super(QTypeSignal, self).__init__()
        
    def run(self):
        # 發射訊號(emit 傳遞字串參數)
        self.sendmsg.emit("第一個參數", "第二個參數")
        
# 槽物件(接收者)
class QTypeSlot(QObject):
    
    def __init__(self):
        super(QTypeSlot, self).__init__()
        
    # 槽物件裡的槽函數
    def get(self, msg1, msg2):
        print("QSlot get msg =>" + msg1 + " " + msg2)
        
    def test(self, msg):
        print("Test msg =>" + msg)
        
if __name__ == "__main__":
    
    print("")
    send = QTypeSignal()
    slot = QTypeSlot()
    
    # 1 
    print("--- 把訊號連結到槽函數 get() 上 ---")
    # 連結訊號與槽(2/5): 連結訊號與槽函數。
    send.sendmsg.connect(slot.get)
    send.run() # 執行發射訊號
    
    # 2 
    print("--- 斷開訊號與槽函數 get() 的連結 ，因此收不到訊號 ---")
    send.sendmsg.disconnect(slot.get)
    send.run() # 發射訊號不會被執行
    
    