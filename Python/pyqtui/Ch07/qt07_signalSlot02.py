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
# 本例介紹第三類方法: 裝飾器訊號與槽的使用以及其他訊號與槽的進階用法
# 
# 進階自訂指的是以自己喜歡的方式定義訊號與槽函數，並傳遞參數，流程如下:
# 1. 定義訊號
# 2. 定義槽函數
# 3. 連結訊號與槽函數
# 4. 發射訊號
#
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import (pyqtSignal, QObject)

class CustSignal(QObject):
    
    # 宣告無參數的訊號
    signal1 = pyqtSignal()
    # 宣告帶一個int類型的訊號
    signal2 = pyqtSignal(int)
    # 宣告帶int和str類型參數的訊號
    signal3 = pyqtSignal(int, str)
    # 宣告帶一個列表類型參數的訊號
    signal4 = pyqtSignal(list)
    # 宣告帶一個字典類型參數的訊號
    signal5 = pyqtSignal(dict)
    # 宣告一個多重版本的訊號，包括帶(int, str)類型參數的訊號，以及帶str類型參數的訊號
    signal6 = pyqtSignal([int, str], [str])
    

    # 槽函數定義
    def signalCall1(self):
        print("signal 1 emit")
        
    def signalCall2(self, intval):
        print("signal 2 emit, value:", intval)
    
    def signalCall3(self, intval, strval):
        print("signal 3 emit, value:", intval, strval)
        
    def signalCall4(self, listval):
        print("signal 4 emit, value:", listval)
        
    def signalCall5(self, dictval):
        print("signal 5 emit, value:", dictval)
        
    def signalCall6(self, intval, strval):
        print("signal 6 emit, value:", intval, strval)
        
    def signalCall6Overload(self, strval):
        print("signal 6 overload emit, value:", strval)
        
    def __init__(self, parent = None):
        super(CustSignal, self).__init__(parent)
        
        # 將訊號連結到指定槽函數
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        self.signal6[int, str].connect(self.signalCall6)
        self.signal6[str].connect(self.signalCall6Overload)
        
        # 發射訊號
        self.signal1.emit()
        self.signal2.emit(2)
        self.signal3.emit(3, "Three")
        self.signal4.emit([4, 44, 444])
        self.signal5.emit({"55": 55, "5555": 5555})
        self.signal6[int, str].emit(6, "six")
        self.signal6[str].emit("six Overload")
    
if __name__ == "__main__":
    custSignal = CustSignal()
    