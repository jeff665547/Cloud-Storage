# PyQt5 進階介面控制項 
# 網頁互動
# PyQt5 使用 QWebEngineView 控制項呈現 HTML 頁面，並且不再維護舊版的QWebView類別，
# 因為 QWebEngineView 透過 Chromium 核心，帶給使用者更好的體驗。
# Qt 慢慢淘汰古老的 WebKit ，取而代之的是WebEngine框架。
# WebEngine 是基於 Google 的 Chromium 引擎開發而來，也就是內部整合了Chromium引擎。
# WebEngine框架封裝Chromium的 Content API ，投入的成本比較小，可以完善地支援HTML5
# 在PyQt5中，可以透過PyQt5.QtWebKitWidgets.QWebEngineView類別使用網頁控制項。
# QWebEngineView控制項使用load()函數載入Web頁面，實際上就是以HTTP GET方法讀取Web頁面。
# 這個控制項可載入本地的Web頁面，也能夠載入遠端的外部Web頁面。
# 另外，QWebEngineView控制項還能使用setHtml()函數，以便設定HTML的內容。
# 此例展示如何在QWebEngineView載入本地local端的Web頁面。

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle("Load and print the local webpage")
        self.setGeometry(5, 30, 555, 330)
        self.browser = QWebEngineView()
        # Load the local webpage
        url = "C:/Users/jeff/Desktop/pyqtui/Ch05/YouTube.html"
        self.browser.load(QUrl( url ))
        self.setCentralWidget(self.browser)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())