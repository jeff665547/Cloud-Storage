# PyQt5 訊號與槽
# 訊號與槽有三種使用方法:
# 1. 內建訊號與槽的使用
# 2. 自訂訊號與槽的使用
# 3. 裝飾器訊號與槽的使用 (為第1種方法的衍伸)
#
# 本例接續介紹第三類方法: 裝飾器訊號與槽的使用
# 所謂裝飾器與槽，就是透過裝飾器的方法定義訊號和槽函數。
# 
# @PyQt5.QtCore.pyqtSlot(參數)
# def on_發送者物件名稱_發射訊號名稱(self, 參數):
#     pass
#
# 這種方法生效的前提是已經執行下面的函數:
# QtCore.QMetaObject.connectSlotByName(QObject)
# 其意義簡單來說是 PyQt5 根據訊號名稱自動連接槽函數的核心程式碼，詳細一點說明是將
# QObject 子孫物件的某些訊號，按照(子孫物件)其objectName連接到對應的槽函數
# 
# 在上述程式碼中，"發送者物件名稱"就是以setObjectName設定的名稱，
# 因此自訂槽函數的命名規則也可視為: On + 以setObjectName設定的名稱 + 訊號名稱。
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QPushButton)

class CustWidget( QWidget ):
    
    def __init__(self, parent = None):
        super(CustWidget, self).__init__(parent)
        
        self.okButton = QPushButton("OK", self)
        
        # 以 setObjectName 設定物件名稱
        self.okButton.setObjectName("okButton")
        
        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)
        
        QtCore.QMetaObject.connectSlotsByName(self)
        
    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print("按下了OK按鈕")
        
    # 因為執行了QtCore.QMetaObject.connectSlotsByName(self)，因此此段函數程式碼
    # 會被自動識別為下面的程式碼
    # def __init__(self, parent = None):
    #              
    #          ...
    #          
    #    QtCore.QMetaObject.connectSlotsByName(self)
    #    self.okButton.clicked.connect(self.okButton_clicked)
    #
    # def okButton_clicked(self):
    #    print("按下了OK按鈕")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CustWidget()
    win.show()
    app.exec_()