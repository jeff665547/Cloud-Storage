# 利用事件處理機制解決多執行緒問題
# 對於極耗時的程式來說，由於PyQt需要等待程式執行完畢才能執行下一步，
# 這個過程呈現在介面上就是lag。
# 如果在執行耗時的程式時，不斷地呼叫QApplication.processEvents(),
# 就可以達到一邊執行耗時程式，一邊刷新頁面的功能，帶來程式運行極為流暢的感覺。
# 因此，QApplication.processEvents()的使用方法便是：在主函數執行耗時的地方，
# 加入QApplication.processEvents()。

from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, 
                             QListWidget, QGridLayout)
import sys
import time

class WinForm(QWidget):
    
    def __init__(self, parent = None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("即時刷新頁面範例")
        self.listFile = QListWidget()
        self.btnStart = QPushButton("Start")
        
        layout = QGridLayout(self)
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)
        
        self.btnStart.clicked.connect(self.slotAdd)
        self.setLayout(layout)
        
    def slotAdd(self):
        
        for n in range(10):
            str_n = "File index {0}".format(n)
            self.listFile.addItem(str_n)
            
            # 此處為程式耗時的地方(程式重複執行)
            # 不斷地呼叫QApplication.processEvents(),
            # 來刷新頁面，帶來程式運行極為流暢的感覺。
            QApplication.processEvents()
            
            time.sleep(1)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())