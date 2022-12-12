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
# 此例展示如何在QWebEngineView載入並顯示嵌入的HTML標記
# 換句話說，就是把index.html的內容直接寫在PyQt script中。
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle("Load and print the local webpage")
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        
        # 載入並且顯示嵌入的HTML標記
        #　注意：　以QWebEngineView物件的setHtml()函數渲染HTML頁面時，如果其內使用的
        # JavaScript腳本超過2MB，頁面就會渲染失敗，出面大片的空白，詳見QTBUG-5414 
        # (https://bugreports.qt.io/browse/QTBUG-53414) 此處可查看Bug資訊以及官方回饋。

        self.browser.setHtml('''
            <!DOCTYPE html>
            <html>
                    <head>
                            <meta charset = "UTF-8">
                            <title></title>
                    </head>
                    <body>
                            <h1>Hello PyQt5</h1>
                            <h1>Hello PyQt5</h1>
            <h1>hello PyQt5</h1>
            <h1>hello PyQt5</h1>
            <h1>hello PyQt5</h1>
            <h1>hello PyQt5</h1>
                    
                    </body>
            </html>
            
            ''')
        
        self.setCentralWidget(self.browser)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())