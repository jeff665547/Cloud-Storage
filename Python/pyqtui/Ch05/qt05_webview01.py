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
# 此例展示如何在QWebEngineView載入外部的Web頁面。

# import PyQt5.QtWebEngineWidgets 時要做的事情，否則會出錯
"""
def webengine_hack():
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication.instance()
    if app is not None:
        import sip
        app.quit()
        sip.delete(app)
    import sys
    from PyQt5 import QtCore, QtWebEngineWidgets
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.qApp = QtWidgets.QApplication(sys.argv)
    return app

try:
    # just for testing
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication([''])
    from PyQt5 import QtWebEngineWidgets
except ImportError as exception:
    print('\nRetrying webengine import...')
    app = webengine_hack()
    from PyQt5 import QtWebEngineWidgets
"""
####### Start ###############
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle("An Example of Opening Online Webpage.")
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        # Load online webpage
        self.browser.load(QUrl("http://www.youtube.com"))
    
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()
