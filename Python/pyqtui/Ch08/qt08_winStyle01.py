# PyQt5 圖形與特效
# 在本例中，展示如何設定視窗樣式。(無邊框圖片檔)
# 注意:執行時必須在獨立執行，不能一邊開啟Spyder一邊執行此程式

from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.resize(400, 200)
        self.setWindowTitle("Set the windows style example")
        # 設定無邊框視窗樣式
        self.setWindowFlags( Qt.FramelessWindowHint )
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(C:/Users/jeff/Desktop/pyqtui/Ch08/image1.jpg);}")
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    