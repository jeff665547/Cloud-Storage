# PyQt5 圖形與特效
# 不規則的視窗顯示
# 用一張遮罩圖片(mask.png)控制視窗的大小以及形狀，再利用paintEvent()函數重繪
# 視窗的背景圖片，圖片會在遮罩中黑色的地方顯現出來。
#
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch08")
import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import (QPixmap, QPainter, QBitmap)

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("不規則視窗的實作範例")
        
        self.pix = QBitmap("./mask.png")
        self.resize(self.pix.size())
        self.setMask(self.pix)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        # 在指定區域直接繪製視窗背景
        painter.drawPixmap(0, 0, self.pix.width(), 
                           self.pix.height(), QPixmap("./image1.jpg"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
