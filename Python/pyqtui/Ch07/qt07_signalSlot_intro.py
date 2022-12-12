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
from PyQt5.QtCore import pyqtSignal

# 1. 定義訊號
# 透過類別成員變數定義訊號物件
class MyWidget(QWidget):
    
    # 無參數的訊號
    Signal_NoParameters = pyqtSignal()
    
    # 帶一個參數(整數)的訊號
    Signal_OneParameter = pyqtSignal(int)
    
    # 帶一個參數(整數或字串)，重載版本的訊號
    Signal_OneParameter_Overload = pyqtSignal([int], [str])
    
    # 帶兩個參數(整數, 字串)的訊號
    Signal_TwoParameters = pyqtSignal(int, str)
    
    # 帶兩個參數([整數, 整數]或[整數、字串])，重載版本的訊號
    Signal_TwoParameters_Overload = pyqtSignal([int, int], [int, str])
    
# 2. 定義槽函數
# 定義一個槽函數，它有多個不同的輸入參數
class MyWidget(QWidget):
    
    def setValue_NoParameters(self):
        """無參數的槽函數"""
        pass
    
    def setValue_OneParameter(self, nIndex):
        """帶一個參數(整數)的槽函數"""
        pass

    def setValue_OneParameter_String(self, szIndex):
        """帶一個參數(字串)的槽函數"""
        pass
    
    def setValue_TwoParameters(self, x, y):
        """帶兩個參數(整數, 整數)的槽函數"""
        pass
    
    def setValue_TwoParameters_String(self, x, szY):
        """帶兩個參數(整數, 字串)的槽函數"""
        pass
    
# 3. 連結訊號與槽函數
# 透過connect方法連結訊號與槽函數(或可呼叫的物件)
app = QApplication(sys.argv)
widget = MyWidget()

# 連結無參數的訊號
widget.Signal_NoParameters.connect(self.setValue_NoParameters)

# 連結帶一個整數參數的訊號
widget.Signal_OneParameter.connect(self.setValue_OneParameter)

# 連結帶一個整數參數，經過重載的訊號
widget.Signal_OneParameter_Overload[int].connect(setValue_OneParameter)

# 連結帶一個字串參數，經過重載的訊號
widget.Signal_OneParameter_Overload[str].connect(self.setValue_OneParameter_String)

# 連結一個訊號，它有兩個整數參數
widget.Signal_TwoParameters.connect(self.setValue_TwoParameters)

# 連結帶兩個參數(整數，整數)，重載版本的訊號
widget.Signal_TwoParameters_Overload[int, int].connect(self.setValue_TwoParameters)

# 連結帶兩個參數(整數、字串)，重載版本的訊號
widget.Signal_TwoParameters_Overload[int, str].connect(self.setValue_TwoParameters_String)

widget.show()

# 4. 發射訊號
# 透過emit方法發射訊號
class MyWidget(QWidget):
    
    def mousePressEvent(self, event):
        
        # 發射無參數的訊號
        self.Signal_NoParameters.emit()
        
        # 發射帶一個參數(整數)的訊號
        self.Signal_OneParameter.emit(1)
        
        # 發射帶一個參數(整數)，重載版本的訊號
        self.Signal_OneParameter_Overload.emit(1)
        
        # 發射帶一個參數(字串)，重載版本的訊號
        self.Signal_OneParameter_Overload.emit("abc")
        
        # 發射帶兩個參數(整數、字串)的訊號
        self.Signal_TwoParameters.emit(1, "abc")
        
        # 發射帶兩個參數(整數、整數)，重載版本的訊號
        self.Signal_TwoParameters_Overload.emit(1, 2)
        
        # 發射帶兩個參數(整數、字串)，重載版本的訊號
        self.Signal_TwoParameters_Overload.emit(1, "abc")
        