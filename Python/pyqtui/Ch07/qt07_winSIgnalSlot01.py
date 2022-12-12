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
# 本例介紹第一種方法: 內建訊號與槽的使用
# 內建訊號與槽的使用指在發射訊號時呼叫視窗控制項的函數，而不是自訂的函數
# 透過QObject.signal.connect將一個QObject的訊號連接到另一個QObject的槽函數。
import os
import sys
from PyQt5.QtWidgets import (QPushButton, QApplication, QWidget,
                             QMessageBox)

def showMsg():
    QMessageBox.information(widget, "訊息提示框", "OK彈出測試訊息")

app = QApplication(sys.argv)
widget = QWidget()

btn = QPushButton("測試點擊按鈕", widget)
btn.clicked.connect(showMsg)

# 訊號與槽機制:
# 發送者 --> 訊號 -> connect(連接) -> 接收
#  -> 接收者 --> 呼叫 -> 槽函數
#
# 發送者: btn (QPushButton)
# 訊號: clicked
# 接收者: QMessageBox
# 槽函數: information

widget.show()
sys.exit(app.exec_())