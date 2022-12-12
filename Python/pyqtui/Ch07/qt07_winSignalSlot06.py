# PyQt5 訊號與槽
# 傳遞視窗資料
# 開發程式時，若程式只有一個視窗，只需關心視窗裡面各個控制項之間如何傳遞資料
# 若有多個視窗，那麼得需關心不同視窗之間如何傳遞資料。
# 對於多視窗資料的傳遞，一般有兩種解決辦法。
# 1. 由主視窗取得子視窗控制項的屬性
# 2. 透過訊號與槽機制，子視窗以發射訊號的形式傳遞資料，
#    再由主視窗的槽函數接收這些資料。
#
# 本例先示範回顧一下單一視窗的資料傳遞
# 對單一視窗來說，一個控制項的改變，將影響另一個控制項的變化。
# 利用訊號與槽的機制，非常容易解決此情境的問題
import os
import sys
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)
from PyQt5.QtCore import Qt

class WinForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        # 先建立滑塊和LCD控制項
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        
        # 透過QVBoxLayout設定佈局
        vBox = QVBoxLayout()
        vBox.addWidget(lcd)
        vBox.addWidget(slider)
        
        self.setLayout(vBox)
        
        # valueChanged() 是QSlider的一個訊號函數，只要slider的值發生改變，
        # 它就會發射一個訊號，然後透過connect連接接收端的控制項，也就是lcd
        slider.valueChanged.connect(lcd.display)
        
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle("訊號與槽 連接滑塊 LCD")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())