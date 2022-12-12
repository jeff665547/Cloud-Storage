import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# 首先彈出一個視窗，然後在10秒之後消失。

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel("<font color = red size = 128><b>Hello PyQt 視窗會在10秒後消失 </b></font>")
    
    # 無邊框視窗
    label.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
    
    label.show()
    
    # 設定10秒後自動退出
    QTimer.singleShot(10000, app.quit)
    # QTimer.singleShot: 在指定的時間間隔呼叫一個槽函數時，發射此訊號。
    
    sys.exit(app.exec_())
    