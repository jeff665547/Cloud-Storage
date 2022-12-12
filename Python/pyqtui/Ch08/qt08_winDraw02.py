# PyQt5 圖形與特效
# 繪圖
# 雙緩衝繪圖
# 本例示範在畫板上繪製矩形，包括雙緩衝繪圖的概念
# 本例首先在畫布上繪製圖形，然後將畫布繪製到視窗中。
# 執行程式，以滑鼠拖出一個矩形，當拖動的速度越快，重影變越少。
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("Draw Rectangle Example")
        
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUI()
        
    def initUI(self):
        # 設定視窗大小600*500
        self.resize(600, 500)
        # 設定畫布大小400*400，背景為白色
        self.pix = QPixmap(400, 400)
        self.pix.fill(Qt.white)
        
    #1 覆寫paintEvent()函數，加上初始化作業，亦即透過lastPoint和endPoint
    #  兩個點，藉以確定繪製矩形的起點、寬度和高度。
    def paintEvent(self, event):
        painter = QPainter(self)
        x = self.lastPoint.x()
        y = self.lastPoint.y()
        w = self.endPoint.x() - x
        h = self.endPoint.y() - y
        
        pp = QPainter(self.pix)
        pp.drawRect(x, y, w, h)
        painter.drawPixmap(0, 0, self.pix)
        
    def mousePressEvent(self, event):
        # 按下滑鼠左鍵
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
    
    def mouseMoveEvent(self, event):
        # 然後移動滑鼠游標
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            # 重新繪製
            self.update()
            
    def mouseReleaseEvent(self, event):
        # 釋放滑鼠左鍵
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # 重新繪製
            self.update()
            
if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
