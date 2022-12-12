import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Qthread 使用情境：
# 在此程式中，按一下 "Testing" 按鈕後，程式頁面直接 "停止回應" ，
# 直到迴圈結束之後才重新更新，於是計時器始終顯示0。

# 在PyQt中，所有的視窗都位於UI主執行緒(就是執行QApplication.exec()的執行緒)。
# 在這個執行緒執行耗時的操作會阻塞UI執行緒，進而讓視窗停止回應。如果視窗長時間
# 沒有回應，便會影響使用者體驗，更嚴重的會導致程式崩潰。因此，為了避免出現這樣的問題，
# 請改用QThread開啟一個新的執行緒，然後在這個執行緒完成耗時的操作。(qt05_thread02.py)

global sec # set global variable
sec = 0

def setTime():
    global sec
    sec += 1
    # LED顯示數字 + 1
    lcdNumber.display(sec)
    
def work():
    # 計時器每秒計數
    timer.start(1000)
    for i in range(2000000000):
        pass
    
    time.stop()
    
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
    # 每次計時結束，觸發setTime
    timer.timeout.connect(setTime)
    button.clicked.connect(work)
    
    top.show()
    sys.exit(app.exec_())