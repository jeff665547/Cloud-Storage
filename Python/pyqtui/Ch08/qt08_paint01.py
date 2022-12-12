# PyQt5 圖形與特效
# 不規則的視窗顯示
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch08")
import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import (QPixmap, QPainter, QBitmap)

class MyForm(QWidget):
    def __init__(self, parent = None):
        super(MyForm, self).__init__(parent)
        self.setWindowTitle("不規則視窗的實作範例")
        
    def paintEvent(self, event):
        painter = QPainter(self)
        # 繪製左半部
        painter.drawPixmap(0, 0, 280, 390, QPixmap(r"./image1.jpg"))
        # 繪製右半部
        painter.drawPixmap(300, 0, 280, 390, QBitmap(r"./image1.jpg"))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())