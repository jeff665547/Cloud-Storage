# PyQt5 訊號與槽
# 開發程式時經常會執行一些耗時的操作，導致介面停頓，這也就是多執行續派上用場之處--
# 為了解決這個問題，可以建立多個執行緒，利用主執行緒更新介面，再以子執行緒即時處理資料，
# 最後將結果顯示於介面上。
# 本例定義一個後台執行緒類別BackendThread，用來模擬後台耗時的作業，
# 這個執行緒類別定義了訊號update_date。利用BackendThread執行緒類別在幕後處理資料，
# 然後每秒發射一次自訂訊號update_date。
# 初始化視窗介面後，定義後台執行緒類別BackendThread，並把執行緒類別的訊號update_date
# 連接到槽函數handleDisplay()。如此一來，後台執行緒每發射一次訊號，就能夠把最新的時間值
# 即時顯示於前台視窗的QLineEdit文字方塊中。

from PyQt5.QtCore import (QThread, pyqtSignal, QDateTime)
from PyQt5.QtWidgets import (QApplication, QDialog, QLineEdit)
import time
import sys

class BackendThread(QThread):
    # 透過類別成員物件定義訊號
    update_date = pyqtSignal(str)
    
    # 處理商業邏輯
    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currTime))
            time.sleep(1)
            
class Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("PyQt5介面即時更新範例")
        self.resize(400, 100)
        self.input = QLineEdit(self)
        self.input.resize(400, 100)
        self.initUI()
        
    def initUI(self):
        # 建立執行緒
        self.backend = BackendThread()
        # 連結訊號
        self.backend.update_date.connect(self.handleDisplay)
        # 開始執行緒
        self.backend.start()
        
    # 輸出目前時間到文字方塊
    def handleDisplay(self, data):
        self.input.setText(data)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())