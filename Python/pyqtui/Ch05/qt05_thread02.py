# 在此例中，主介面有一個用來顯示時間的LCD數字面板，還有一個啟動任務(跑迴圈)的按鈕，
# 按下 testing 的按鈕後會開始跑2000000000次的迴圈，用來模擬耗時的工作。
# 若不使用Qthread或是其他多執行緒的方式來處理，會導致程式介面直接停止回應。
# 如果視窗長時間沒有回應，便會影響使用者體驗，更嚴重的會導致程式崩潰。
# 為了避免此問題發生，使用QThread開啟一個新的執行緒，在這個執行緒完成耗時的操作。
# 讓 LCD 面板顯示的數字和迴圈耗時操作分別同步獨立執行

# QThread 和 主視窗 使用一般的訊號與槽機制來做溝通
# 即利用 pyqtSignal() 以及 共用的屬性存取 來做溝通

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

global sec
sec = 0

class WorkThread(QThread):
    trigger = pyqtSignal()
    def __init__(self):
        super(WorkThread, self).__init__()
        
    def run(self):
        
        # 待執行的迴圈耗時操作
        for i in range(2000000000):
            # print(i)
            pass
        
        # 迴圈完畢後發射訊號
        self.trigger.emit()
        
def countTime():
    global sec
    sec += 1
    # LED 顯示數字 + 1
    lcdNumber.display(sec)
        
def work():
    # 計時器每秒計數
    timer.start(1000)
    # 計時開始
    
    workThread.start()
    # 利用QThread.start()啟動一個新的執行緒
    # 呼叫start()函數之後即可啟動執行緒。
    # 接著執行緒會自動執行實作(workThread)的run方法，
    # 該方法(run())就是執行緒背後的執行函數。
    # 耗時的操作(商業邏輯)會放在run()函數內，
    # 當run()退出後，基本上執行緒就結束了。
    
    # 當收到迴圈完畢的訊號時，停止計數
    workThread.trigger.connect(timeStop)
    
def timeStop():
    timer.stop()
    print("執行結束 耗時", lcdNumber.value())
    global sec
    sec = 0
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(300, 120)
    # 垂直布局類別QVBoxLayout
    layout = QVBoxLayout(top)
    # 增加一個顯示面板
    lcdNumber = QLCDNumber()
    layout.addWidget(lcdNumber)
    button = QPushButton("Testing")
    layout.addWidget(button)
    
    timer = QTimer()
    workThread = WorkThread()
    
    button.clicked.connect(work)
    # 每次計時結束，觸發countTime
    timer.timeout.connect(countTime)
    
    top.show()
    sys.exit(app.exec_())
    