# 利用 QThread 來改寫QApplication.processEvents()的範例。

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
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
        
        # self.tt = work()
        
    def slotAdd(self):
        
        self.tt = work()
        self.tt2 = work2()
        self.tt2.pa = 6
        
        for n in range(10):
            print("start")
            str_n = "File index {0}".format(n)
            self.listFile.addItem(str_n)
            
            # self.tt = work() # 這行不能放在這裡，
                               # 因為此範圍屬於local variable區域
            
            # self.tt.start()
        
        self.tt2.setpar(666)
        self.tt2.start()

class work(QThread):
    def __init__(self):
        super(work, self).__init__()
        
    def run(self):
        
        for j in range(10):
            # print(j)
            pass
            
class work2(QThread):
    def __init__(self):
        super(work2, self).__init__()
        self.pa = 0
    
    def setpar(self, par):
        self.pa = par
    
    def run(self):
        for i in range(10):
            print("A")
            print(self.pa)
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())