# QThread 和 主視窗 使用一般的訊號與槽機制來做溝通
# 即利用 pyqtSignal() 以及 共用的屬性存取 來做溝通

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MainWidget(QWidget):
    def __init__(self, parent = None):
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle("QThread example")
        
        # 建立一個新的執行續
        self.thread = Worker()
        
        self.listFile = QListWidget()
        self.btnStart = QPushButton('Start')
        layout = QGridLayout(self)
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)
        self.btnStart.clicked.connect(self.slotStart)
        self.thread.sinOut.connect(self.slotAdd)
        
    def slotAdd(self, file_inf):
        self.listFile.addItem(file_inf)
        
    def slotStart(self):
        self.btnStart.setEnabled(False)
        self.thread.start()
        
class Worker(QThread):
    sinOut = pyqtSignal(str)
    
    def __init__(self, parent = None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0
        
    def __del__(self):
        self.working = False
        # self.wait()
        
    def run(self):
        #　執行續相關的程式碼
        while self.working == True:
            file_str = "File index {0}".format(self.num)
            self.num += 1
            # 發射訊號
            self.sinOut.emit(file_str)
            # 執行緒休眠2秒
            self.sleep(2)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWidget()
    demo.show()
    sys.exit(app.exec_())
    