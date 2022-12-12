# PyQt5 圖形與特效
# 設定視窗背景
# 視窗背景主要包括:背景顏色和背景圖片，設定視窗背景有三種方法
# 1. 以QSS設定視窗背景
# 2. 以QPalette設定視窗背景
# 3. 實作paintEvent，再以QPainter繪製背景。
# 本例示範以paintEvent設定視窗背景顏色。
# 
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("paintEvent Background Color Setting")
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.yellow)
        
        # Set the background color.
        painter.drawRect(self.rect())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())