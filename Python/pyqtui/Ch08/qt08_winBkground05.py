# PyQt5 圖形與特效
# 設定視窗背景
# 視窗背景主要包括:背景顏色和背景圖片，設定視窗背景有三種方法
# 1. 以QSS設定視窗背景
# 2. 以QPalette設定視窗背景
# 3. 實作paintEvent，再以QPainter繪製背景。
# 本例示範以paintEvent設定視窗背景圖片。
# 
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch08")
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import (QPainter, QPixmap)
import sys

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("paintEvent Background Color Setting")
        
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("./image1.jpg")
        
        # 繪製視窗背景圖片，平鋪到整個視窗，隨著視窗的改變而改變
        painter.drawPixmap(self.rect(), pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())