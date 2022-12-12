# PyQt5 進階介面控制項 
# 網頁互動
# JavaScript呼叫PyQt程式碼 (雙向互動)
# PyQt可以與載入的Web頁面進行雙向的資料互動。
# 將QWebEngineView物件載入Web頁面後，便可取得表單輸入的資料。
# 在Web頁面中，通常是透過JavaScript腳本收集使用者提交的資料；然後，JavaScript藉由
# 橋接方式傳遞資料給PyQt。當PyQt收到頁面傳遞的資料，經過邏輯處理後，還能把處理過的
# 資料返回Web頁面。
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch05")
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from MySharedObject import MySharedObject
from PyQt5.QtWebChannel import QWebChannel
import sys

# 建立一個應用程式實例
app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("Web頁面的JavaScript與QWebEngineView互動範例")

# 建立一個垂直布局器
layout = QVBoxLayout()
win.setLayout(layout)

# 建立一個QWebEngineView物件
view = QWebEngineView()
htmlUrl = "C:/Users/jeff/Desktop/pyqtui/Ch05/web/index.html"
view.load(QUrl(htmlUrl))

# 建立一個QWebChannel物件，用來傳遞PyQt的參數到JavaScript
channel = QWebChannel()
myObj = MySharedObject()
channel.registerObject("bridge", myObj)
view.page().setWebChannel(channel)

# 把QWebEngineView控制項載入layout佈局
layout.addWidget(view)

# 顯示視窗和執行
win.show()
sys.exit(app.exec_())