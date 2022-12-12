# PyQt5 圖形與特效
# 在本例中，展示如何使用自訂的無邊框視窗。(全螢幕藍屏)
# 注意:執行時必須在獨立執行，不能一邊開啟Spyder一邊執行此程式

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    '''自訂視窗類別'''
    def __init__(self, parent = None):
        '''Constructor'''
        # 呼叫父類別constructor
        super(MyWindow, self).__init__(parent)
        
        # 設定視窗標誌(無邊框)
        self.setWindowFlags( Qt.FramelessWindowHint )
        
        # 為便於顯示，設定視窗背景顏色(採用QSS)
        self.setStyleSheet('''background-color:blue; ''')
        
    def showMaximized(self):
        '''最大化視窗'''
        # 取得桌面控制項
        desktop = QApplication.desktop()
        # 取得螢幕可顯示尺寸
        rect = desktop.availableGeometry()
        # 設定視窗尺寸
        self.setGeometry(rect)
        # 顯示視窗
        self.show()
        
if __name__ == "__main__":
    
    # 宣告變數
    app = QApplication(sys.argv)
    # 建立視窗
    window = MyWindow()
    # 最大化顯示
    window.showMaximized()
    # 應用程式事件迴圈
    sys.exit(app.exec_())
    